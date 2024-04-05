# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHirestec(RPackage):
	"""Non-Targeted Fluxomics on High-Resolution Mass-Spectrometry Data

	Identifying labeled compounds in a 13C-tracer experiment in
    non-targeted fashion is a cumbersome process. This package facilitates
    such type of analyses by providing high level quality control plots,
    deconvoluting and evaluating spectra and performing a multitude of
    tests in an automatic fashion.  The main idea is to use changing
    intensity ratios of ion pairs from peak list generated with 'xcms' as
    candidates and evaluate those against base peak chromatograms and
    spectra information within the raw measurement data automatically.
    The functionality is described in Hoffmann et al. (2018)
    <doi:10.1021/acs.analchem.8b00356>.
	"""
	
	homepage = "https://github.com/janlisec/HiResTEC"
	cran = "HiResTEC" 

	version("0.62.3", md5="7e28033a653983193241064c1b4c121a")
	version("0.62", md5="d03a8de575f1e7bf186363974959f8de")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-beeswarm", type=("build", "run"))
	depends_on("r-cormid", type=("build", "run"))
	depends_on("r-interpretmsspectrum", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
