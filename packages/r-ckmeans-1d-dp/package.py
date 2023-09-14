# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCkmeans1dDp(RPackage):
    """Fast, optimal, and reproducible weighted univariate clustering by dynamic programming."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://cran.r-project.org/web/packages/Ckmeans.1d.dp/index.html"
    cran = "Ckmeans.1d.dp"

    version("4.3.5", sha256="a30599db8bc1c77f20b3b9193772c60e713232a6f4aa6ac68c5569a0b6bc403d")
    version("4.3.4", sha256="4691b5b55a91f9f2fb6a2e2b77a3017c62ab9f4e0ca6a928af1f8ef3acba29d3")
    version("4.3.3", sha256="a6145ed6c56a95641be30037b89208d9fa683855beaf960396ecd3fb76d5084c")
    version("4.3.2", sha256="3fbf0f7409990574074ac33d663abf83f6e1f68d09b2d6ac55ecb6fea09cd7a3")
    version("4.3.0", sha256="b329df64c157640cc93f77c84b1018ebbdea8cccaf69161652a27a4fd4418576")
    version("4.2.2", sha256="b08aba3fbf1741b60786bdc4fa96e42c29d001559354b86197fba383efe55995")
    version("4.2.1", sha256="1f2d9320ec4e2994358c38b787a962789154cea84dba4960c7a530915320a5cb")
    version("4.2.0", sha256="4c319d68fc94b28467db198a00dadba901171301d0c76d041f1c6e62ae8018a2")
    version("4.0.1", sha256="383f1b1a2d601cbdfc935f1245f41b6d64268f3a69091a908fe3c486be761e91")
    version("4.0.0", sha256="bdfbe6899d906649a6b41f079dfeaeaf9eba44763f1fa5d9a8c86776dfc18648")
    version("3.4.6-6", sha256="9dc85b619594ea41468919a735b0157a61b9f89bdcae580b5ce7f4d0ddb73934")
    version("3.4.6-5", sha256="51ffce6f0c4c97114aaad12e3d9159d4edc027af9963bea6cd8b5b749500314f")
    version("3.4.6-4", sha256="d1151c2bc32a694c4d431d5f4942079226f222429e0e1c27264947f5e3a4fbec")
    version("3.4.6-3", sha256="e9917f71e5bfa2a7fda62e98849be3fbcd87b3a62d1c0976f1cb95a8c82d8b6e")
    version("3.4.6-2", sha256="785858f35ee975eab69b99a635b5d3f0473823b5a2b8f85bfd8a27c22459ee93")
    version("3.4.6-1", sha256="46c02b752ac716b75d3e17129c9f5bdee35084ef3e7617ef7956f812b46a3358")
    version("3.4.6", sha256="872c212962aaa8589e5a7ef78c695efa16b63be68518f9e8fa7c54bf740c037e")
    version("3.4.0-1", sha256="7122997c95838a42c41bf6920c099eaaa716c352c9ea78758d6bd95d942ac9ce")
    version("3.4.0", sha256="7ffb0e30a13a4275b7bc186e6871bfcbc9c351ece44dc5b4a1b899c5dc97728a")
    version("3.3.3", sha256="2e3c9e8a14c758cac8f43e54082226a70ad5374c42fd64d49cc8033320d22740")
    version("3.3.1", sha256="c9e1298857b6d18c0dfc720b4f62ee728e84088e385a4fc1c83bdce1cc63fc3f")
    version("3.3.0", sha256="4a0b65dfa129db5ee01a6bfbf5eae5360cecf047eb91dd22721582fd180b46ee")
    version("3.02", sha256="053f9d425e362fb802643ff8ae69f18041cb703d595a474e448f22cbf2eeffe4")
    version("3.01", sha256="73db074715693cea18456a7a0cbc83213291b0fe7d1d721ff78c553ec9d626b4")
    version("3.0", sha256="ba93e4cc54a0eccc8523279dc3c415648a0fa0aa4d32d03d3a177e42ca4660a8")
    version("2.5", sha256="d31cdcbd4f24bdd24f085e80375b2d12b2f20abbb84685e6d13a0e48ca8081d2")
    version("2.4", sha256="161c7aeae58a26bbf8ebd5cda187557d721a44b82dbf0d5d9af71b1f583b6b70")
    version("2.3", sha256="8e31cc4e473247ce37d61b2cb567b6f705984156db4ab900425570008115f443")
    version("2.2", sha256="7606bc2cc50b966a92205bc192b35d27ac1471e27c31b9055f82095e7225cb6e")
    version("2.1", sha256="0dd4676cecb2cd0e8b37f6df81a71520cbc9302cd4fda682395a07148ade512a")
    version("2.0", sha256="12429d59a98af24690b76b391fce2eb4bc070e3aa6f9214ae6f9e1abc2aff655")
    version("1.1", sha256="2f38f92e3f946abbf105b6f6045fa333a2e1eb5eb06481cee0f5a69d70eefb36")
    version("1.0", sha256="d5cea457c6f876c709a5b34772c7c992ca5a0b4ff86c5c481b044878726dc574")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rdpack", type=("build", "run"))
