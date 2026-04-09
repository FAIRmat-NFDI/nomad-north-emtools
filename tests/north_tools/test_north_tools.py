def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails
    from nomad_north_emtools.north_tools import emtools

    assert emtools.id_url_safe == 'emtools' or emtools.id == 'nomad-north-emtools', (
        'NORTHTool entry point has incorrect id or id_url_safe'
    )
