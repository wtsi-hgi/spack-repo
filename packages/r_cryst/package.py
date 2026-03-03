# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCryst(RPackage):
	"""Calculate the Relative Crystallinity of Starch by XRD and FTIR

	Functions to calculate the relative crystallinity of starch by X-ray Diffraction (XRD) and Infrared Spectroscopy (FTIR). Starch is biosynthesized by plants in the form of granules semicrystalline. For XRD, the relative crystallinity is obtained by separating the crystalline peaks from the amorphous scattering region. For FTIR, the relative crystallinity is achieved by setting of a Gaussian holocrystalline-peak in the 800-1300 cm-1 region of FTIR spectrum of starch which is divided into amorphous region and crystalline region. The relative crystallinity of native starch granules varies from 14 of 45 percent. This package was supported by FONDECYT 3150630 and CIPA Conicyt-Regional R08C1002 is gratefully acknowledged.
	"""
	
	cran = "cryst" 

	version("0.1.0", md5="3a430e5bd2745492865528b6e29addfd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-flux", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
