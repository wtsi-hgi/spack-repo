# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChisqPosthocTest(RPackage):
	"""A Post Hoc Analysis for Pearson's Chi-Squared Test for Count
Data

	Perform post hoc analysis based on residuals of Pearson's Chi-squared Test for Count Data based on T. Mark Beasley & Randall E. Schumacker (1995) <doi: 10.1080/00220973.1995.9943797>.
	"""
	
	homepage = "http://chisq-posthoc-test.ebbert.nrw/"
	cran = "chisq.posthoc.test" 

	version("0.1.2", md5="ea3bb29d75a10ae1e15bea3b0fa37221")

