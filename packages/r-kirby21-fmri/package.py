# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKirby21Fmri(RPackage):
	"""Example Functional Imaging Data from the Multi-Modal MRI
'Reproducibility' Resource

	Functional magnetic resonance imaging ('fMRI')
       data from the 'Kirby21' 'reproducibility' study
       <doi:10.1016/j.neuroimage.2010.11.047>.
	"""
	
	homepage = "https://www.nitrc.org/projects/multimodal/"
	cran = "kirby21.fmri" 

	version("1.7.0", md5="0723e3d505a4afbeec61a6c7a105c20f")

	depends_on("r-kirby21-base@1.7:", type=("build", "run"))
