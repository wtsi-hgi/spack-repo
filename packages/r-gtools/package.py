# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtools(RPackage):
	"""Various R Programming Tools.

	Functions to assist in R programming.
	Including:
	[1] assist in developing, updating, and maintaining R and R packages
	('ask', 'checkRVersion', 'getDependencies', 'keywords', 'scat');
	[2] calculate the logit and inverse logit transformations ('logit',
	'inv.logit');
	[3] test if a value is missing, empty or contains only NA and NULL values
	('invalid');
	[4] manipulate R's .Last function ('addLast');
	[5] define macros ('defmacro');
	[6] detect odd and even integers ('odd', 'even');
	[7] convert strings containing non-ASCII characters (like single
	 quotes) to plain ASCII ('ASCIIfy');
	[8] perform a binary search ('binsearch');
	[9] sort strings containing both numeric and character components
	('mixedsort');
	[10] create a factor variable from the quantiles of a continuous variable
	('quantcut');
	[11] enumerate permutations and combinations ('combinations',
	'permutation');
	[12] calculate and convert between fold-change and log-ratio ('foldchange',
	'logratio2foldchange', 'foldchange2logratio');
	[13] calculate probabilities and generate random numbers from Dirichlet
	distributions ('rdirichlet', 'ddirichlet');
	[14] apply a function over adjacent subsets of a vector ('running');
	[15] modify the TCP_NODELAY ('de-Nagle') flag for socket objects;
	[16] efficient 'rbind' of data frames, even if the column names don't match
	('smartbind');
	[17] generate significance stars from p-values ('stars.pval');
	[18] convert characters to/from ASCII codes;
	"""

	cran = "gtools"

	license("GPL-2.0-only")

	version("3.9.5", md5="6d7837a6d8b8019e16a7c9eb567899db")

