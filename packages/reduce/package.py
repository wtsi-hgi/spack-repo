# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Reduce(CMakePackage):
    """Reduce - tool for adding and correcting hydrogens in PDB files"""

    homepage = "https://github.com/rlabduke/reduce"
    url = "https://github.com/rlabduke/reduce/archive/refs/tags/v4.14.tar.gz"

    version("4.14", sha256="62e61cce221fff76b5834031302d91fe703a19945a42e16620d4fb860604daf4")

    depends_on("boost", type=("build", "link"))
    depends_on("python", type=("build", "link", "run"))
