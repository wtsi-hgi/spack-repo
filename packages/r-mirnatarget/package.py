# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirnatarget(RPackage):
    """gene target tabale of miRNA for human/mouse used for MiRaGE package

    gene target tabale of miRNA for human/mouse used for MiRaGE package
    """

    bioc = "miRNATarget"

    version("1.46.0", commit="cf3a85a06b24089ecb4d55c375a25dbcbba1ba45")
    version("1.40.0", commit="f29b74050b61c41b5ede0e0600fd132fb6c81731")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
