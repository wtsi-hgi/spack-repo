# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTorchopt(RPackage):
	"""Advanced Optimizers for Torch

	Optimizers for 'torch' deep learning library. These
    functions include recent results published in the literature and are
    not part of the optimizers offered in 'torch'. Prospective users
    should test these optimizers with their data, since performance
    depends on the specific problem being solved.  The packages includes
    the following optimizers: (a) 'adabelief' by Zhuang et al (2020),
    <arXiv:2010.07468>; (b) 'adabound' by Luo et al.(2019),
    <arXiv:1902.09843>; (c) 'adahessian' by Yao et al.(2021)
    <arXiv:2006.00719>; (d) 'adamw' by Loshchilov & Hutter (2019),
    <arXiv:1711.05101>; (e) 'madgrad' by Defazio and Jelassi (2021),
    <arXiv:2101.11075>; (f) 'nadam' by Dozat (2019),
    <https://openreview.net/pdf/OM0jvwB8jIp57ZJjtNEZ.pdf>; (g) 'qhadam' by
    Ma and Yarats(2019), <arXiv:1810.06801>; (h) 'radam' by Liu et al.
    (2019), <arXiv:1908.03265>; (i) 'swats' by Shekar and Sochee (2018),
    <arXiv:1712.07628>; (j) 'yogi' by Zaheer et al.(2019),
    <https://papers.nips.cc/paper/8186-adaptive-methods-for-nonconvex-optimization>. 
	"""
	
	homepage = "https://github.com/e-sensing/torchopt/"
	cran = "torchopt" 

	version("0.1.4", md5="238ae689141f694e87f955b21cd5e7ec")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
