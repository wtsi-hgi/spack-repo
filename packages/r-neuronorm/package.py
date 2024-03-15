# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeuronorm(RPackage):
	"""Preprocessing of Structural MRI for Multiple Neurodegenerative
Diseases

	Preprocessing pipeline for normalizing and cleaning T1-weighted, T2-weighted and FLAIR MRI images coming from different sources, diseases, patients, scanners and sites.
	"""
	
	cran = "neuronorm" 

	version("1.0.2", md5="1e5b833c3c6b7c3442aa3e4a6706d6ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-fslr", type=("build", "run"))
	depends_on("cmake", type=("build", "link", "run"))
	depends_on("fsl", type=("build", "link", "run"))
