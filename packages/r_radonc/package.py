# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadonc(RPackage):
	"""Analytical Tools for Radiation Oncology

	Designed for the import, analysis, and visualization of dosimetric and volumetric data in Radiation Oncology, the tools herein enable import of dose-volume histogram information from multiple treatment planning system platforms and 3D structural representations and dosimetric information from 'DICOM-RT' files.  These tools also enable subsequent visualization and statistical analysis of these data.
	"""
	
	cran = "RadOnc" 

	version("1.1.8", md5="773302cedd29e63a3c8914f32ed1d964")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-oro-dicom@0.5:", type=("build", "run"))
	depends_on("r-ptinpoly", type=("build", "run"))
