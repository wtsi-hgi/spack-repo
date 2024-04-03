# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniversalcvi(RPackage):
	"""Hard and Soft Cluster Validity Indices

	Algorithms for checking the accuracy of a clustering result with known classes, computing cluster validity indices, and generating plots for comparing them.
    The package is compatible with K-means, fuzzy C means, EM clustering, and hierarchical clustering (single, average, and complete linkage).
    The details of the indices in this package can be found in:
    C. Alok. (2010) <https://hdl.handle.net/10603/93443>,
    J. C. Bezdek, M. Moshtaghi, T. Runkler, C. Leckie (2016) <doi:10.1109/TFUZZ.2016.2540063>,
    T. Calinski, J. Harabasz (1974) <doi:10.1080/03610927408827101>,
    C. H. Chou, M. C. Su, E. Lai (2004) <doi:10.1007/s10044-004-0218-1>,
    D. L. Davies, D. W. Bouldin (1979) <doi:10.1109/TPAMI.1979.4766909>,
    J. C. Dunn (1973) <doi:10.1080/01969727308546046>,
    F. Haouas, Z. Ben Dhiaf, A. Hammouda, B. Solaiman (2017) <doi:10.1109/FUZZ-IEEE.2017.8015651>,
    M. Kim, R. S. Ramakrishna (2005) <doi:10.1016/j.patrec.2005.04.007>,
    S. H. Kwon (1998) <doi:10.1049/EL:19981523>,
    S. H. Kwon, J. Kim, S. H. Son (2021) <doi:10.1049/ell2.12249>,
    G. W. Miligan (1980) <doi:10.1007/BF02293907>,
    M. K. Pakhira, S. Bandyopadhyay, U. Maulik (2004) <doi:10.1016/j.patcog.2003.06.005>,
    M. Popescu, J. C. Bezdek, T. C. Havens, J. M. Keller (2013) <doi:10.1109/TSMCB.2012.2205679>,
    S. Saitta, B. Raphael, I. Smith (2007) <doi:10.1007/978-3-540-73499-4_14>,
    A. Starczewski (2017) <doi:10.1007/s10044-015-0525-8>,
    Y. Tang, F. Sun, Z. Sun (2005) <doi:10.1109/ACC.2005.1470111>,
    N. Wiroonsri (2024) <doi:10.1016/j.patcog.2023.109910>,
    N. Wiroonsri, O. Preedasawakul (2023) <arXiv:2308.14785>,
    C. H. Wu, C. S. Ouyang, L. W. Chen, L. W. Lu (2015) <doi:10.1109/TFUZZ.2014.2322495> and
    X. Xie, G. Beni (1991) <doi:10.1109/34.85677>.
	"""
	
	cran = "UniversalCVI" 

	version("1.1.2", md5="3827ddb00112a576bd80c5e35cbff974")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
