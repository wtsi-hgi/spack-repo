# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgascores(RPackage):
	"""Score Taxon-Level IgA Binding in IgA-Seq Experiments

	Functions to calculate indices used to score immunoglobulin A (IgA) binding of bacteria in IgA sequencing (IgA-Seq) experiments.
  This includes the original Kau and Palm indices and more recent methods as described in Jackson et al. (2020) <doi:10.1101/2020.08.19.257501>.
  Additionally the package contains a function to simulate IgA-Seq data and an example experimental data set for method testing. 
	"""
	
	homepage = "https://doi.org/10.1101/2020.08.19.257501"
	cran = "IgAScores" 

	version("0.1.2", md5="9a1ec1db3d8ed5ec955537f714cc442f")

	depends_on("r@3.5:", type=("build", "run"))
