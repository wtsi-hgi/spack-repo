# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestassay(RPackage):
	"""A Hypothesis Testing Framework for Validating an Assay for
Precision

	A common way of validating a biological assay for is through a
    procedure, where m levels of an analyte are measured with n replicates at each
    level, and if all m estimates of the coefficient of variation (CV) are less
    than some prespecified level, then the assay is declared validated for precision
    within the range of the m analyte levels. Two limitations of this procedure are:
    there is no clear statistical statement of precision upon passing, and it is
    unclear how to modify the procedure for assays with constant standard deviation.
    We provide tools to convert such a procedure into a set of m hypothesis tests.
    This reframing motivates the m:n:q procedure, which upon completion delivers
    a 100q% upper confidence limit on the CV. Additionally, for a post-validation
    assay output of y, the method gives an ``effective standard deviation interval''
    of log(y) plus or minus r, which is a 68% confidence interval on log(mu), where
    mu is the expected value of the assay output for that sample. Further, the m:n:q
    procedure can be straightforwardly applied to constant standard deviation assays.
    We illustrate these tools by applying them to a growth inhibition assay. This is
    an implementation of the methods described in Fay, Sachs, and Miura (2018) 
    <doi:10.1002/sim.7528>.
	"""
	
	cran = "testassay" 

	version("0.1.1", md5="63951eeafe611353eabda36796e0382a")

	depends_on("r@3.5:", type=("build", "run"))
