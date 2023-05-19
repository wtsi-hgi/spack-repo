# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class AegScrambler(PythonPackage):
    """Analyse and rank genomic data."""

    homepage = "https://github.com/wtsi-hgi/aeg-scrambler"
    
    depends_on("pridict", type=("build", "run"))
    