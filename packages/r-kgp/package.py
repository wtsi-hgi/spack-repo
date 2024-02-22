# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKgp(RPackage):
	"""1000 Genomes Project Metadata

	Metadata about populations and data about samples from the 1000 Genomes Project, including the 2,504 samples sequenced for the Phase 3 release and the expanded collection of 3,202 samples with 602 additional trios. The data is described in Auton et al. (2015) <doi:10.1038/nature15393> and Byrska-Bishop et al. (2022) <doi:10.1016/j.cell.2022.08.004>, and raw data is available at <http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/>. See Turner (2022) <doi:10.48550/arXiv.2210.00539> for more details.
	"""
	
	homepage = "https://github.com/stephenturner/kgp"
	cran = "kgp" 

	version("1.1.1", md5="a508d3d57e5bcf4464290f8b36077c4b")

	depends_on("r@2.10:", type=("build", "run"))
