# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsMachineLearning(RPackage):
	"""'Amazon Web Services' Machine Learning Services

	Interface to 'Amazon Web Services' machine learning services,
    including 'SageMaker' managed machine learning service, natural
    language processing, speech recognition, translation, and more
    <https://aws.amazon.com/machine-learning/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.machine.learning" 

	version("0.5.0", md5="e9324edccd144378319eb4c1dd83ac9c")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
