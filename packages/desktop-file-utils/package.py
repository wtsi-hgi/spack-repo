# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class DesktopFileUtils(MesonPackage):
    """desktop-file-utils contains a few command line utilities for working with desktop entries."""

    homepage = "https://www.freedesktop.org/wiki/Software/desktop-file-utils/"
    url = "https://www.freedesktop.org/software/desktop-file-utils/releases/desktop-file-utils-0.28.tar.xz"

    version("0.28", sha256="4401d4e231d842c2de8242395a74a395ca468cd96f5f610d822df33594898a70")
    version("0.27", sha256="a0817df39ce385b6621880407c56f1f298168c040c2032cedf88d5b76affe836")
    version("0.26", sha256="b26dbde79ea72c8c84fb7f9d870ffd857381d049a86d25e0038c4cef4c747309")
    version("0.25", sha256="438199400333300fb8a14033d7c2f24ce3cf2e300312da9ff0b3337e35d06b8e")
    version("0.24", sha256="a1de5da60cbdbe91e5c9c10ac9afee6c3deb019e0cee5fdb9a99dddc245f83d9")
    version("0.23", sha256="6c094031bdec46c9f621708f919084e1cb5294e2c5b1e4c883b3e70cb8903385")
    version("0.22", sha256="843532672692f98e9b2d6ae6cc8658da562dfde1606c7f33d9d227a344de56c5")
    version("0.21", sha256="b6c9b860538ef1cffbcdfbc9cb578f85a080ad8c1207c8b3a39e9fd183f9782b")
    version("0.20", sha256="a7507379859cc483f1c64fbdb569f722c75e3af7c3f91bcdc239ff9dacd24f49")
    version("0.19", sha256="1f805c44fc6943d2d9d2acfe2aa4c6edc1fa17b1807e4e950c8ce50111ddc81b")

    depends_on("glib@2:")
