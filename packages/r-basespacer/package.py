# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasespacer(RPackage):
	"""R SDK for BaseSpace RESTful API

	A rich R interface to Illumina's BaseSpace cloud computing environment, enabling the fast development of data analysis and visualisation tools.
	"""
	
	bioc = "BaseSpaceR"

	version("1.52.0", commit="57aab245d83348f1fd62a52a4319880274a0caf2")
	version("1.46.0", commit="517fb8f188aa9c918dfa84318e1612c4adc825c2")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
