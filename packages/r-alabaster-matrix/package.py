# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterMatrix(RPackage):
    """Load and Save Artifacts from File

    Save matrices, arrays and similar objects into file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
    """

    bioc = "alabaster.matrix"

    version("1.8.0", commit="2c0db5db4ce24a06c3af229ec763b55dc8dd79c6")
    version("1.2.0", commit="7c9f38142b5899f52d8b5f06a600aa22a03b5072")

    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
    depends_on("r-sparsearray", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-alabaster-base", type=("build", "run"))
