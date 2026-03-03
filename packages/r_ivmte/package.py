# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvmte(RPackage):
	"""Instrumental Variables: Extrapolation by Marginal Treatment
Effects

	The marginal treatment effect was introduced by Heckman and
    Vytlacil (2005) <doi:10.1111/j.1468-0262.2005.00594.x> to provide a
    choice-theoretic interpretation to instrumental variables models that
    maintain the monotonicity condition of Imbens and Angrist (1994)
    <doi:10.2307/2951620>. This interpretation can be used to extrapolate from
    the compliers to estimate treatment effects for other subpopulations. This
    package provides a flexible set of methods for conducting this
    extrapolation. It allows for parametric or nonparametric sieve estimation,
    and allows the user to maintain shape restrictions such as monotonicity. The
    package operates in the general framework developed by Mogstad, Santos and
    Torgovitsky (2018) <doi:10.3982/ECTA15463>, and accommodates either point
    identification or partial identification (bounds). In the partially
    identified case, bounds are computed using either linear programming
    or quadratically constrained quadratic programming. Support for
    four solvers is provided. Gurobi and the Gurobi R API
    can be obtained from <http://www.gurobi.com/index>. CPLEX can be obtained
    from <https://www.ibm.com/analytics/cplex-optimizer>. CPLEX R APIs 'Rcplex'
    and 'cplexAPI' are available from CRAN. MOSEK and the MOSEK R API can be
    obtained from <https://www.mosek.com/>. The lp_solve library is freely
    available from <http://lpsolve.sourceforge.net/5.5/>, and is included when
    installing its API 'lpSolveAPI', which is available from CRAN.
	"""
	
	cran = "ivmte" 

	version("1.4.0", md5="19bfb89b93ffd8f27fb8adeba55e037d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
