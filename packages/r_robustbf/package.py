# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustbf(RPackage):
	"""Robust Solution to the Behrens-Fisher Problem

	Robust tests (RW and RF) are provided for testing the equality of two long-tailed symmetric (LTS) means when the variances are unknown and arbitrary. RW test is a robust version of Welch's two sample t test and the RF is a robust fiducial based test. The RW and RF tests are proposed using the adaptive modified maximum likelihood (AMML) estimators derived by Tiku and Surucu (2009) <doi:10.1016/j.spl.2008.12.001> and Donmez (2010) <https://open.metu.edu.tr/bitstream/handle/11511/19440/index.pdf>.
	"""
	
	cran = "RobustBF" 

	version("0.2.0", md5="67cf249e154b9c94696a18f9456e8c05")

