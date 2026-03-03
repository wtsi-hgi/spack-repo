# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdin(RPackage):
	"""ODE Generation and Integration

	Generate systems of ordinary differential equations
    (ODE) and integrate them, using a domain specific language
    (DSL).  The DSL uses R's syntax, but compiles to C in order to
    efficiently solve the system.  A solver is not provided, but
    instead interfaces to the packages 'deSolve' and 'dde' are
    generated.  With these, while solving the differential equations,
    no allocations are done and the calculations remain entirely in
    compiled code.  Alternatively, a model can be transpiled to R for
    use in contexts where a C compiler is not present.  After
    compilation, models can be inspected to return information about
    parameters and outputs, or intermediate values after calculations.
    'odin' is not targeted at any particular domain and is suitable
    for any system that can be expressed primarily as mathematical
    expressions.  Additional support is provided for working with
    delays (delay differential equations, DDE), using interpolated
    functions during interpolation, and for integrating quantities
    that represent arrays.
	"""
	
	homepage = "https://github.com/mrc-ide/odin"
	cran = "odin" 

	version("1.2.5", md5="550661eeb178a73c2faf557cac51f709")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-cinterpolate@1:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ring", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
