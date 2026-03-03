# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKirby21T1(RPackage):
	"""Example T1 Structural Data from the Multi-Modal MRI
'Reproducibility' Resource

	Structural T1 magnetic resonance imaging ('MRI')
       data from the 'Kirby21' 'reproducibility' study
       <doi:10.1016/j.neuroimage.2010.11.047>.
	"""
	
	homepage = "https://www.nitrc.org/projects/multimodal/"
	cran = "kirby21.t1" 

	version("1.7.0", md5="b313301062b91187ba12f139547fe180", url="https://cran.r-project.org/src/contrib/kirby21.t1_1.7.0.tar.gz")

	depends_on("r-kirby21-base@1.7:", type=("build", "run"))
