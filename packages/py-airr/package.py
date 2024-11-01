# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAirr(PythonPackage):
    """AIRR Community Data Representation Standard reference library for antibody and TCR sequencing data."""

    homepage = "http://docs.airr-community.org"
    pypi = "airr/airr-1.5.1.tar.gz"

    version(
        "1.1.0",
        sha256="7f43b80abcf9c31d714fdea0c9900b8c391c67afe96088d282b651fbbed6e8a2",
    )
    version(
        "1.2.0",
        sha256="187d8ad2a24e4c36ce7fba0a3d9ce7f4f9bfd8f410ff37e466a5f112ec359fb8",
    )
    version(
        "1.2.1",
        sha256="b6c523cee7822b327bfcc637e6261bda27a0d4148bc46a73fef745199ee5fcb9",
    )
    version(
        "1.3.0",
        sha256="fe85883a4e8b81871d377edd7ac09aa95b576b9e98996938fda4dab119cbad10",
    )
    version(
        "1.3.1",
        sha256="f71912de693033516798dbbabef5a855987ce417dbac9054894e88648bacd15a",
    )
    version(
        "1.4.1",
        sha256="52276f977b31694751f7cc2d56d50843ac7b363883e7daac60130a5abe839ed9",
    )
    version(
        "1.5.0",
        sha256="febc0a881bf46b1a9c29ac6a7089dd733ff9120d114585e75dede26403f68d42",
    )
    version(
        "1.5.1",
        sha256="71f89eaf0c2fb4fe038a6e8aad9c58e1712cb06b92021e73d97d08c59b7b7149",
    )

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-yamlordereddictloader", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-sigprofilersinglesample", type=("build", "run"))
