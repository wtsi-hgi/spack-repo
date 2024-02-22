# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaepirtparams(RPackage):
	"""IRT Parameters for the National Assessment of Education Progress

	This data package contains the Item Response Theory (IRT) parameters for the National Center for Education Statistics (NCES) items used on the National Assessment of Education Progress (NAEP) from 1990 to 2015. The values in these tables are used along with NAEP data to turn student item responses into scores and include information about item difficulty, discrimination, and guessing parameter for 3 parameter logit (3PL) items. Parameters for Generalized Partial Credit Model (GPCM) items are also included. The adjustments table contains the information regarding the treatment of items (e.g., deletion of an item or a collapsing of response categories), when these items did not appear to fit the item response models used to describe the NAEP data. Transformation constants change the score estimates that are obtained from the IRT scaling program to the NAEP reporting metric. Values from the years 2000 - 2013 were taken from the NCES website <https://nces.ed.gov/nationsreportcard/> and values from 1990 - 1998 and 2015 were extracted from their NAEP data files. All subtest names were reduced and homogenized to one word (e.g. "Reading to gain information" became "information"). The various subtest names for univariate transformation constants were all homogenized to "univariate".
	"""
	
	cran = "NAEPirtparams" 

	version("1.0.0", md5="04d92b1eb177f054c86b01acf81fc6aa")

	depends_on("r@3.5:", type=("build", "run"))
