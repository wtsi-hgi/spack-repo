# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterString(RPackage):
    """Save and Load Biostrings to/from File

    Save Biostrings objects to file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
    """

    bioc = "alabaster.string"

    version("1.8.0", commit="cdede3f44e9632a68902e401219f09c6db773a0a")
    version("1.2.0", commit="51fce8086e5ac447f0e74fd0ee0c71cb7f97b3f1")

    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-alabaster-base", type=("build", "run"))
