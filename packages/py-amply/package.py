# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAmply(PythonPackage):
    """Amply allows you to load and manipulate AMPL/GLPK data as Python data structures"""

    homepage = "http://github.com/willu47/amply"
    pypi = "amply/amply-0.1.6-py3-none-any.whl"

    version("0.1", sha256="52af4823e48dcfae495f4af09920b6fd4289d3957768714681a754bec85ec5d8")
    version("0.1.0a6", sha256="cdb86c8946d566dffec9570d252baf21de1b0aa3cd29f477be21ef6fa1f2ac48")
    version("0.1.0a7", sha256="88864703ee10c8ac1dfd7b78321f96634d14797c21437ae38e89cc7bad1b2fb2")
    version("0.1.1", sha256="e37188b4faab2f78f2452026976394a9cb766a0cd109acc46359be02d3c125fb")
    version("0.1.2", sha256="6e5d53af62772790ba82a989a3de72b8ce5c1cd809613c06f7cb061f7ec34dc8")
    version(
        "0.1.4",
        sha256="f8a846a544750493f45e75e9b44c393144be5728701df4f596b1fa5595d263fd",
        expand=False,
        url="https://files.pythonhosted.org/packages/f3/c5/dfa09dd2595a2ab2ab4e6fa7bebef9565812722e1980d04b0edce5032066/amply-0.1.4-py3-none-any.whl",
    )
    version(
        "0.1.5",
        sha256="57a1141b2591614c69df35f1df2f7913b8f5d5330aae92ce1b4b73ae8905fe6a",
        expand=False,
        url="https://files.pythonhosted.org/packages/eb/97/c7e61ca87316e5e498066c53681a4586f9666ef32f027e58b7c2b755fa68/amply-0.1.5-py3-none-any.whl",
    )
    version(
        "0.1.6",
        sha256="44c372cf60dbdfda06e80cbf201a28d1e6384485b6a2386ca21160dccd0e82a8",
        expand=False,
        url="https://files.pythonhosted.org/packages/43/b1/5ff785027761a1d29d6fabbad15fe5d9327a38bc2a1eb753f9d467bbbb5d/amply-0.1.6-py3-none-any.whl",
    )

    depends_on("py-pyparsing", type=("build", "run"))
    depends_on("py-docutils", type=("build", "run"))


# {'docutils(>=0.3)': ['0.1.4', '0.1.5', '0.1.6'], 'pyparsing': ['0.1.4', '0.1.5', '0.1.6']}
