# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAegScrambler(PythonPackage):
    """Analyse and rank genomic data."""

    homepage = "https://github.com/wtsi-hgi/aeg-scrambler"

    version("0.0.1", commit="aec9152b76a561781456c5bfe03411c761fab598")
    
    #depends_on("py-pridict", type=("build", "run"))
    depends_on("py-pyranges", type=("build", "run"))
    depends_on("typer", type=("build", "run"))
    depends_on("scipy", type=("build", "run"))
    depends_on("scikit-learn", type=("build", "run"))
    depends_on("pandas", type=("build", "run"))
    depends_on("pyyaml", type=("build", "run"))
