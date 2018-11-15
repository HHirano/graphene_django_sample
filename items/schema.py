import graphene
from graphene_django import DjangoObjectType
from items.models import Items


class Item(DjangoObjectType):
    class Meta:
        model = Items


class CreateItem(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        count = graphene.Int()

    item = graphene.Field(lambda :Item)

    def mutate(self, info, name, count):
        item = _get_or_create(Items, name=name, count=count)
        return CreateItem(item=item)


class UpdateItem(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        count = graphene.Int()

    item = graphene.Field(lambda :Item)

    def mutate(self, info, id, name, count):
        item = _update(Items, id=id, name=name, count=count)
        return UpdateItem(item=item)


class Query(graphene.ObjectType):
    items = graphene.List(Item)

    def resolve_items(self, info, **kwargs):
        return Items.objects.all()


class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
    update_item = UpdateItem.Field()


def _get_or_create(kls, **kwargs):
    """
    create object if not exists
    """
    try:
        instance = kls.objects.get(**kwargs)
    except:
        instance = kls.objects.create(**kwargs)
    return instance


def _update(kls, **kwargs):
    """
    update object
    """
    try:
        id = int(kwargs.get('id', None))
        instance = kls.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    except kls.DoesNotExist:
        raise



