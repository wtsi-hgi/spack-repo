# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyrad(RPackage):
	"""Genotype Calling with Uncertainty from Sequencing Data in
Polyploids and Diploids

	Read depth data from genotyping-by-sequencing (GBS) or restriction 
  site-associated DNA sequencing (RAD-seq) are imported and used to make Bayesian
  probability estimates of genotypes in polyploids or diploids.  The genotype 
  probabilities, posterior mean genotypes, or most probable genotypes can then
  be exported for downstream analysis.  'polyRAD' is described by Clark et al.
  (2019) <doi:10.1534/g3.118.200913>, and the Hind/He statistic for marker
  filtering is described by Clark et al. (2022) <doi:10.1186/s12859-022-04635-9>.
  A variant calling pipeline for highly duplicated genomes is also included and
  is described by Clark et al. (2020, Version 1) <doi:10.1101/2020.01.11.902890>.
	"""
	
	homepage = "https://github.com/lvclark/polyRAD"
	cran = "polyRAD" 

	version("2.0.0", md5="2a5919b7d3a253131debb576c8457501")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
