# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearnrbook(RPackage):
	"""Datasets and Code Examples from P. J. Aphalo's "Learn R" Book

	Data, scripts and code from chunks used as examples in the book 
   "Learn R: As a Language" by Pedro J. Aphalo.
   ISBN 9780367182533 (pbk); ISBN 9780367182557 (hbk); ISBN 9780429060342 (ebk).
	"""
	
	homepage = "https://docs.r4photobiology.info/learnrbook/"
	cran = "learnrbook" 

	version("1.0.2-1", md5="7fb6dffe2133a5e71e48a1746a0f7083")

	depends_on("r@3.6:", type=("build", "run"))
