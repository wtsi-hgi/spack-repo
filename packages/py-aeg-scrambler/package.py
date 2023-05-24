# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAegScrambler(PythonPackage):
    """Analyse and rank genomic data."""

    git = "https://github.com/wtsi-hgi/aeg-scrambler"

    version("0.0.1", sha256="47ce194b03b90e6f7cf6567193773a06d41f3b02")
    
    #depends_on("py-pridict", type=("build", "run"))
    #depends_on("py-pyranges", type=("build", "run"))
    depends_on("py-typer", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
