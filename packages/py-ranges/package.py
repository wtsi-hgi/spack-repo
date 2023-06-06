# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRanges(PythonPackage):
    """GenomicRanges for Python."""

    git = "https://github.com/pyranges/pyranges"

    version("0.0.127", sha256="458397177c39823999fc175eed89852369ae8463")
    
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-ncls", type=("build", "run"))
    depends_on("py-tabulate", type=("build", "run"))
    depends_on("py-sorted_nearest", type=("build", "run"))
    depends_on("py-natsort", type=("build", "run"))