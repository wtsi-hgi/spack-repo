# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySinfo(PythonPackage):
    """sinfo outputs version information for modules loaded in the current session, Python, and the OS."""

    homepage = "https://gitlab.com/joelostblom/sinfo"
    pypi = "sinfo/sinfo-0.3.4.tar.gz"

    version("0.1", sha256="f9f88a6278c3799d8d26764233cfab209886b580746d1eaf8636a22c7d59c916")
    version("0.1.1", sha256="cdf7aa9682997fbb557bbdccaa051578ceaf04e91511d12887368037b3298e8f")
    version("0.1.2", sha256="e32959ddfec49e8779efd82bd14902f86d1c895435de2dc98e792f2b06bf4088")
    version("0.1.3", sha256="a07f5bcb14c8a6c085b473febb93918a32222c54c352e74a0de9895bf7655f67")
    version("0.1.4", sha256="b9d5ac26dc7a4f54330a937543462d6c1eb17498881b691b5ebb3e561baf991b")
    version("0.2.0", sha256="11d48919e68f474e4258822dd7aa39dcb5c90ebdb9a171ddc5651a85c2b73a62")
    version("0.3.0", sha256="81cebf6828f9559c2db35b2b4f8c04dd50929fc7454ba7f907469fb24d7aa00e")
    version("0.3.1", sha256="e1b2358808aded7b2ff00ea0cd4e6a2d978fb2a44ee9b15ac23d64a81bf62706")
    version("0.3.2", sha256="786ebf6e12d6488cb389e2d44ea367ecc3dc4486691ac63752b89526add1d4b3")
    version("0.3.3", sha256="58071167f41d250ebbd2155396cc6614e12dfb1c38aa29ef4ae6ba9ba07a39d5")
    version("0.3.4", sha256="81ea91c69a875de178e10bada9476d7300a1f712e1823dbd7714f43a10baba4d")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
