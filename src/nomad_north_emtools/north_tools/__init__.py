from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

emtools_north_tool = NORTHTool(
    short_description='Use open source software for analyzing electron microscopy data in NOMAD.',
    image='ghcr.io/fairmat-nfdi/nomad-north-emtools:main',
    description="""### **emtools**:

    [hyperspy](https://github.com/hyperspy)

    [Publication about the software](https://zenodo.org/records/18379337)

    [Open Science Award 2025](https://hyperspy.org/news/Award2025.html)""",
    external_mounts=[],
    file_extensions=['ipynb', 'dm3'],
    icon='https://raw.githubusercontent.com/FAIRmat-NFDI/nomad-north-emtools/main/src/nomad_north_emtools/north_tools/emtools/hyperspy.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'markus.kuehbach@physik.hu-berlin.de', 'name': 'Markus Kühbach'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='emtools',
)

emtools = NorthToolEntryPoint(
    id_url_safe='emtools',
    north_tool=emtools_north_tool,
)
