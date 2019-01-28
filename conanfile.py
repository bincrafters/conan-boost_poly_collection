#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostPoly_CollectionConan(base.BoostBaseConan):
    name = "boost_poly_collection"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_poly_collection"
    lib_short_names = ["poly_collection"]
    header_only_libs = ["poly_collection"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_iterator",
        "boost_mp11",
        "boost_mpl",
        "boost_type_erasure",
        "boost_type_traits"
    ]
