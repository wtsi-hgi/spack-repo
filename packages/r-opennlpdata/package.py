# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpennlpdata(RPackage):
	"""Apache OpenNLP Jars and Basic English Language Models

	Apache OpenNLP jars and basic English language models.
	"""
	
	homepage = "https://opennlp.apache.org/"
	cran = "openNLPdata" 

	version("1.5.3-4", md5="00cef2af8eefaa21f26ddf2af2577d2a")

	depends_on("r-rjava@0.6.3:", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
