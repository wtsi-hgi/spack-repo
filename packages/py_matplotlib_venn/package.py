# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMatplotlibVenn(PythonPackage):
    """Functions for plotting area-proportional two- and three-way Venn diagrams in matplotlib."""

    homepage = "https://github.com/konstantint/matplotlib-venn"
    pypi = "matplotlib-venn/matplotlib-venn-1.1.2.tar.gz"

    version("0.10", sha256="6596cf57503791229205ca12b2562c5f39da50763ed1cceff0596da786be2a37")
    version("0.11", sha256="a318041248a5d476e16f4923edc12b1a288eddbe5f69e22f2b740f988276a042")
    version("0.11.1", sha256="0e0ec7deabd92ae62486ba07a81ea7516ae7cc634ecbf69cd27308f006149661")
    version(
        "0.11.10",
        sha256="85650429baff7a812b2785540979e6bf0abcc747e7fe5ffd2a972cb917a826d6",
        expand=False,
        url="https://files.pythonhosted.org/packages/b1/f4/12ea88962cd17acb58bfcce1b93ce256f591698f9adb247de3eea630f590/matplotlib_venn-0.11.10-py3-none-any.whl",
    )
    version("0.11.2", sha256="1bf5ef684882ee98e8dc9631eb8ee1e0356185b3e31fe374d94fe14ca9b5df71")
    version("0.11.3", sha256="a8726dd93651fd771e9290e534148a6fb876f4600e28ef96c36dd64fb7e2709c")
    version("0.11.4", sha256="707d66f923f4c75370c78193b80cc2bd7e417ab149d0373d64d677cc4813f391")
    version("0.11.5", sha256="be017a6821bce410db3314099649f1a0fcf4c0fbf7be0c1190b102187988838f")
    version("0.11.6", sha256="d209a9845bb3a54c4247f1ef3f745e4819660ecc9208137097d2a51281f2a478")
    version("0.11.7", sha256="8d8b3505594313099328c9f177133dd800a28f3dd68e6800a78250c0cccce317")
    version("0.11.8", sha256="1c3520c660b0393748f816448c27b7fc510a33ba39cd50117f0d2a1ddddfdaa4")
    version("0.11.9", sha256="bbf12f2a066c7f8448793b35a307b192004ba4bd8bba133bce09165dbdc9528b")
    version("0.2", sha256="c7fa96c264765f88c255dd34c2af0d7f5c6fb8685ea219eb2886aba4b2c3a0d9")
    version("0.3", sha256="3b5822a48a105620626bf4be38ecd3d2cf726f5fc50869d9ebb64daaed7f39f6")
    version("0.4", sha256="615e5df8e55315aae02a1a3a9a2b693c3720f8b7d32e30b7fe4e787cbdc8e2b5")
    version("0.5", sha256="443f3344a9f52edddf2b9a48342497bed53fbc28d7ede4b4e35fe46d3c1ef89e")
    version("0.6", sha256="2cf2800865bc9ccfd9c058b0c40ecc8a4eb30a39d1ffe17635f26adb999ebc61")
    version("0.7", sha256="7a2d29ba50956052a19de749afbddbd341ffa13b1cfdd7afb5563b4c14538ed3")
    version("0.8", sha256="f52fb2a45b4622a7624576f324fd59afc9e7b366b18214df00b324b3ec3fcffe")
    version("0.9", sha256="577d3ca2ce0b79988539cf3dad9065a3eeb8221bd1c8e366ab49d614888fc09e")
    version("1.0.0", sha256="fde13b525f1147d1f811c8ebafd1ac529515ccaedfaf1f3cecc7476edfbc98ed")
    version(
        "1.0.0a0",
        sha256="a85a46ddf1349fce48aefa3ebd2c55d79e609fcfe9c6dc98f90159f6fcde9064",
        expand=False,
        url="https://files.pythonhosted.org/packages/a3/92/d6d04d5b0582843c6d623f66a0f148470c8bcf07f8b46b23ff8f746d8b4f/matplotlib_venn-1.0.0a0-py3-none-any.whl",
    )
    version("1.1.0", sha256="66cf5638110e79e09bc092e3782f3f6544a5fca282851c6b38e8149e84de01db")
    version("1.1.1", sha256="d885bc015f5091a4b8a8138ff20a7ed166c33b5c36dbc0489f95a5cbc76a2ae5")
    version("1.1.2", sha256="6f2b07a03e9bb5a62de2f32f965216739e175176f9d654dd19e7af2c22ec36e3")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))


# {'matplotlib\r': ['0.11.10'], 'numpy\r': ['0.11.10'], 'scipy\r': ['0.11.10'], 'matplotlib': ['1.0.0a0'], 'numpy': ['1.0.0a0'], 'scipy': ['1.0.0a0']}
