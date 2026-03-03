# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAugmenterr(RPackage):
	"""Data Augmentation for Machine Learning on Tabular Data

	Implementation of a data augmentation technique based on conditional entropy
    It was devised by both authors during their masters and is discussed in detail in the second author dissertation.
    It is able to create novel samples conditioned on a desired value of a categorical attribute, as a way to augment data for classification tasks
    Tests discussed in the dissertation and future paper present that the technique satisfies several statistical assumptions for the novel samples.
    It also shows significant improvement for machine learning models trained on small data.
	"""
	
	cran = "AugmenterR" 

	version("0.1.0", md5="ed12bbdb5bffa108a6723d962b85eed7")

