# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRia(RPackage):
	"""Radiomics Image Analysis Toolbox for Medial Images

	Radiomics image analysis toolbox for 2D and 3D radiological images. RIA supports DICOM, NIfTI,
             nrrd and npy (numpy array) file formats.
             RIA calculates first-order, gray level co-occurrence matrix, gray level run length matrix and
             geometry-based statistics. Almost all calculations are done using vectorized formulas to
             optimize run speeds. Calculation of several thousands of parameters only takes minutes
             on a single core of a conventional PC. Detailed methodology has been published: Kolossvary
             et al. Circ: Cardiovascular Imaging. 2017;10(12):e006843 <doi: 10.1161/CIRCIMAGING.117.006843>.
	"""
	
	homepage = "https://pubmed.ncbi.nlm.nih.gov/29233836/"
	cran = "RIA" 

	version("1.7.2", md5="0d97dbd8b1923f91ec3f6c8b77fb1662")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-oro-dicom@0.5:", type=("build", "run"))
	depends_on("r-oro-nifti@0.9.1:", type=("build", "run"))
