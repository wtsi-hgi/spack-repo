# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoke(RPackage):
	"""Small Molecule Octet/BLI Kinetics Experiment

	Bio-Layer Interferometry (BLI) is a technology to determine the binding kinetics between biomolecules. BLI signals are small and noisy when small molecules are investigated as ligands (analytes). We develop this package to process and analyze the BLI data acquired on Octet Red96 from Fortebio more accurately. 
    Sun Q., Li X., et al (2020) <doi:10.1038/s41467-019-14238-3>. 
    In this new version, we organize the BLI experiment data and analysis methods into a S4 class with self-explaining structure. 
	"""
	
	cran = "smoke" 

	version("2.0.0", md5="44ba02b38c1dde3e05384191eaa57a67")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
