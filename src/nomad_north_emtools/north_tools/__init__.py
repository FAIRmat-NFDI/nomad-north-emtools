from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

emtools = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-emtools.',
    image='ghcr.io/fairmat-nfdi/nomad-north-emtools:main',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-emtools.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'markus.kuehbach@physik.hu-berlin.de', 'name': 'Markus Kühbach'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='emtools',
)

north_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad-north-emtools-emtools',
    north_tool=emtools,
)
