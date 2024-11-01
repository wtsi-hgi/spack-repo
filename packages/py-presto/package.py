# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPresto(PythonPackage):
    """A bioinformatics toolkit for processing high-throughput lymphocyte receptor sequencing data."""

    homepage = "http://presto.readthedocs.io"
    pypi = "presto/presto-0.7.2.tar.gz"

    version(
        "0.5.0",
        sha256="fe5e57171dd3c777a3577823b5e52ca0862cf03f847630efb0d13c421b169a36",
    )
    version(
        "0.5.1",
        sha256="5be967dcdb14a05cdcce270a9976fe8a4263036200232850b9f3e98fdaa17789",
    )
    version(
        "0.5.10",
        sha256="893a6e92f3e1d49a063da74087868e385777f7d9cafb68f9e48131f89c5ca668",
    )
    version(
        "0.5.11",
        sha256="1fd6ef06ec1fe02aec87fecf3ed7bbff39596dab8d55eb0df3c9525921cad80b",
    )
    version(
        "0.5.12",
        sha256="c9d11f93b4ff769642607059bc78ca33bc7b7c7a70a399d0261f707f42d60d7b",
    )
    version(
        "0.5.13",
        sha256="c3cdc4d501d39e5c20593286f2d3ff1c9e341cf4fc751d1bf42858285055b2f4",
    )
    version(
        "0.5.2",
        sha256="dc0cdd1994fc4b7a0d87cedc28c666499fe590f12bba88e06fd3b4518bace241",
    )
    version(
        "0.5.3",
        sha256="7c0df7216ae3dee14e9f31ded22ba06a69cdd4870829745f416edbb28f405d0f",
    )
    version(
        "0.5.4",
        sha256="1c766af10481dd12725370f2dc912fe59e0208b74e449e942a69540243875dc2",
    )
    version(
        "0.5.5",
        sha256="08dbfaf0783fd2a61679a73724e51e5a3dd38690824d6a901d46a3dd06ffba86",
    )
    version(
        "0.5.6",
        sha256="cc0929c0fcf866d4782b52b6cad5389093975c1f30fdeef02d77d9f4c8542ca2",
    )
    version(
        "0.5.7",
        sha256="41ce1b84dad7005681b4ee96ad8df3956db261a89faa9d1cac8db5decc87b7e9",
    )
    version(
        "0.5.8",
        sha256="6eea2926c138596688c25068d19d1455b076a6c4bf5ecdff04cda8e2dc87a015",
    )
    version(
        "0.5.9",
        sha256="127dbeaaf3021acdfb7f541d09e719deae807e047600b32f43e35dd6ecd01fd1",
    )
    version(
        "0.6.0",
        sha256="02b03feac25f26e744a41e00f73847527694e54de73339671679f1520a04d1a8",
    )
    version(
        "0.6.1",
        sha256="556ec60a0c66e6ef0ef594e5e73caee1fa6e4f60f57a793a7c29b294bc621af8",
    )
    version(
        "0.6.2",
        sha256="27b95f393334200376932d72ab2496857ae466fd081a53acbaf3aead34d7cb6a",
    )
    version(
        "0.7.0",
        sha256="b337eb5171c74cbcdbb7a41b01e23c582932455660e01b38192ce9733e7fae36",
    )
    version(
        "0.7.1",
        sha256="8b5787b3a3206fda5e5cd0fd1804a6c0ecb8821f9de2b78d9a5e5a5a31ba43e9",
    )
    version(
        "0.7.2",
        sha256="b4f4b34413af4207eb2052316d31d7bc2067b864286498476d89013ad5423dd9",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
