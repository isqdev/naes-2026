from django.db import migrations


def criar_grupo_gerenciadores(apps, schema_editor):
    grupo = apps.get_model("auth", "Group")
    grupo.objects.get_or_create(name="Gerenciadores")


class Migration(migrations.Migration):
    dependencies = [
        ("tututuru", "0003_adicionar_usuario_aos_cadastros"),
    ]

    operations = [
        migrations.RunPython(criar_grupo_gerenciadores, migrations.RunPython.noop),
    ]
