# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedirection(RPackage):
	"""Predict Dominant Direction of Reactions of a Biochemical Network

	Biologically relevant, yet mathematically sound constraints are used
    to compute the propensity and thence infer the dominant direction of reactions
    of a generic biochemical network. The reactions must be unique and their 
    number must exceed that of the reactants,i.e., reactions >= reactants + 2.  
            'ReDirection', computes the null space of a user-defined stoichiometry
    matrix. The spanning non-zero and unique reaction vectors (RVs) are 
    combinatorially summed to generate one or more subspaces recursively.  
            Every reaction is represented as a sequence of identical components 
    across all RVs of a particular subspace. The terms are evaluated with 
    (biologically relevant bounds, linear maps, tests of convergence, descriptive
    statistics, vector norms) and the terms are classified into forward-, reverse- 
    and equivalent-subsets. Since, these are mutually exclusive the probability 
    of occurrence is binary (all, 1; none, 0).
            The combined propensity of a reaction is the p1-norm of the 
    sub-propensities, i.e., sum of the products of the probability and maximum
    numeric value of a subset (least upper bound, greatest lower bound). This, 
    if strictly positive is the probable rate constant, is used to infer dominant
    direction and annotate a reaction as "Forward (f)", "Reverse (b)" or 
    "Equivalent (e)".
            The inherent computational complexity (NP-hard) per iteration suggests
    that a suitable value for the number of reactions is around 20.
            Three functions comprise ReDirection. These are check_matrix() and 
    reaction_vector() which are internal, and calculate_reaction_vector()
            which is external.
	"""
	
	cran = "ReDirection" 

	version("1.0.1", md5="b1c81e961c1d47c8cf3b3ff2cc663cbb")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
