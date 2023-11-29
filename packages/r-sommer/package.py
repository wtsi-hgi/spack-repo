# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSommer(RPackage):
    """Structural multivariate-univariate linear mixed model solver for estimation of multiple random effects with unknown variance-covariance structures (e.g., heterogeneous and unstructured) and known covariance among levels of random effects (e.g., pedigree and genomic relationship matrices) (Covarrubias-Pazaran, 2016 <doi:10.1371/journal.pone.0156744>; Maier et al., 2015 <doi:10.1016/j.ajhg.2014.12.006>; Jensen et al., 1997). REML estimates can be obtained using the Direct-Inversion Newton-Raphson and Direct-Inversion Average Information algorithms for the problems r x r (r being the number of records) or using the Henderson-based average information algorithm for the problem c x c (c being the number of coefficients to estimate). Spatial models can also be fitted using the two-dimensional spline functionality available."""

    cran = "sommer"

    version("4.3.3", sha256="ec88ddd8241b1c786e19fe1e5756b729dc172d683ced33dc97c360073f75f9ce")
    version("4.3.2", sha256="9efe081895d44a3a3b3d0cea0d4ec144a406dd56029282736980e1092bdc0f10")
    version("4.3.1", sha256="8d5793f08887b7b0980bce07c6c35445d28abaee3a7d88094fe51554bba46479")
    version("4.3.0", sha256="72127f3c1b7271fc173c6cf7eabd41aa31a9f94358034689a6c73192c58d31d2")
    version("4.2.1.2", sha256="19ce58c1ac6f949bda92a425edbe4bef5f7004b74a9394ccf79568c511000af1")
    version("4.2.0.1", sha256="32c913cbcb734938badff7dc0fb10747bf62842dc0e35d3d198dbe78ab5773d8")
    version("4.2.0", sha256="ba1b05d4421513795faced77d792cffc17f351ee374db5c3d065d0edfd6e11c4")
    version("4.1.9", sha256="4dfc9b25d233653b0fa02439a9b1694eb3dd7662d587f421d2becbe01dabe521")
    version("4.1.8", sha256="02e5c64ca688b495b60876df5aab88d1d14542d86078bd695a7b7970c0f3ba74")
    version("4.1.7", sha256="d538d41cd32f0de214d1502db70fb02afa757df667e4127a4fb7b8ebcae85667")
    version("4.1.6", sha256="e8fed96e2135852b23868c086f40460f4bbbf9d237cba50e368fb2bdea2db024")
    version("4.1.5", sha256="fc81227854d97d808e99c8b911dede594991f593749982e1b4e4d69669d7d889")
    version("4.1.4", sha256="a834edbc5d64fffcaa8460c639d52d30f552dd2687b1d7e2c8ff44160a34a5e3")
    version("4.1.3", sha256="acee4ba77ca6933934b61c9e011b398d6602ce5c32c9821bd82501eea33da232")
    version("4.1.2", sha256="73acb2726a981e203130ccc5c3a5e138ca9c5c374ee369b5ebc4537c40748778")
    version("4.1.1", sha256="ded935e224762e7dfd07c572ddff807e9f5e023a49508c9b89bf3a7d7c9e3309")
    version("4.1.0", sha256="c9f276a7f312282925b82b2a769d9484ef0c24f3e55be867ef0e01f224950b29")
    version("4.0.9", sha256="420d5c301c74d0504af1d551918058c63be25befddebdd6780af66618dca2e5b")
    version("4.0.8", sha256="ac9e70859e7b9c4fe4d9622775c3798c02a259f3330433b8904d782274fbf133")
    version("4.0.4", sha256="10c5d04246ba75b6913105c540ba27e895db56a4724bef27e9a5c30ba18ba229")
    version("4.0.1", sha256="9cf7f33c350e05702f0fd7dbfb90a1d4d266dcf700512ef5f33827394102f1fb")
    version("3.9.3", sha256="95848a278b84387ae25dad715f79375f9b45ba8dd5b127821b84dbc0c3649c7a")
    version("3.9.1", sha256="f2c880cec251b646f2482ae72c6e4d64f0a6e2f5dbd9ff4968c7531ccf940c5c")
    version("3.8", sha256="a471dadfe0cf19f04911a8eb108c24bbea4f53c326e4772c7b233e4b61b890f4")
    version("3.7.3", sha256="02e90f5067d3e4b58fdc232165c3ba386db143fbea477155b9f9d5e8cb597341")
    version("3.7.2", sha256="691f8f04309118af8688f7c8393dde2ef6bf551cf0bc07042207a842a142feab")
    version("3.7.1", sha256="79d8af9704b4f29d5a99064e948f8b52c1ef1ce1fc589bde6fb96c21f015d848")
    version("3.7", sha256="632fa8bb18f606649ae3c18b6375560e6244b8a48d4aca17d8aa4f5f0df7d06e")
    version("3.6", sha256="d88045b710ad485b997bf796b2e3aa68a20e0c008c46bba318465021b72ed7fe")
    version("3.5", sha256="3dae3a67b618351c7bdddf1f9b91432d14682da47c2366e7d158bbe185404fe3")
    version("3.4", sha256="53267cace0aa22815c8283eb79fbdc448f481921cdfadc806075dec28166f009")
    version("3.3", sha256="cf76935f09bb5f903aee31b2433b4c991a048b91370d2bb0c24f8c35aa8d03e5")
    version("3.2", sha256="f51ccc7999f7a59dda3044563ab4f59f1a4de41393f817d44a6ce8b11a01134f")
    version("3.1", sha256="e7648e3ffc23643cb51e396a01302205348d4dfdf5486782058076e2ad83202c")
    version("3.0", sha256="1df84dc676849ef0fbd0e931fea44ed213c74fcc4cdae04c0695f2292f71cd49")
    version("2.9", sha256="321afef49adc0e6f3b048387a35249dabf0a44cacb84c36c9831f361d4518504")
    version("2.8", sha256="1b3596c49d221baad8fc6511eed355aa40875c730cc8215464eca1d52b7d0707")
    version("2.7", sha256="0d3c5c1529847928b9388a6ed34251532a571bd98ef76402cf872725dd38c1b2")
    version("2.6", sha256="2e942e22ccc0a9dcd6de266a49e7528d0d6ccea7b4970ba2943f4132a08ac00b")
    version("2.5", sha256="ff0ec70f41eb884fbb8cda1e8a79d5321dedb14f074ffc015cf7df6b07914209")
    version("2.4", sha256="ae35b7e05d8e99ba0c9d3e6de70ab22280b97ca2745eae08c3d7c86095e6431b")
    version("2.3", sha256="152cb19784728cf4f9b764fb50b56acdf52b0876d60dea8bac6fa9c03e4d9416")
    version("2.2", sha256="adfb5950032ce59c186c65fad19b4b6fd7508091cb3f4b0774260c5215eadb46")
    version("2.1", sha256="3f86d1045b094265f26c58cb975950bcb35b17df97dbac721a725238643bb137")
    version("2.0", sha256="dbc4f718e5629174011ff0815d409b64d1fdf8be4fafa9966cf9678ded501670")
    version("1.9", sha256="42ef772024b180990c631b7f969d715597f1bab304679d99202ae76a6e7f2d59")
    version("1.8", sha256="528c961966660494e3593989ada28d2a63ddc1d9283ce479c6cf62d8191e41be")
    version("1.7", sha256="a88fefb833b4f854290bff1b9fbd2c80e378e29aeb8d17c27f340e872b2b931e")
    version("1.6", sha256="8c8a1dd772e1b90488c1b0e45b9dbd79f007a356c296ee2db1259612d968771b")
    version("1.5", sha256="8c504ab2bc9a60005a55a82bee68b0c21400aeb47a70763f5120c1debe61ce43")
    version("1.4", sha256="536e26c38db28985ca0f7a3683d0024e9f5b8b42b60580076cfb47675acafca0")
    version("1.3", sha256="539e7df1b1332b50c747ae2070b10db02c92532181b6d3bdbe93e8e102d63f1b")
    version("1.2", sha256="db85f189933f1db35c2ea7c3220007273b00822a85ed085bd83f1cfc66d19794")
    version("1.1", sha256="b43d53874434f6f03d359a50e9246de69fb8f0e7d1872728f05ef28da7818bba")

    depends_on("r-matrix@1.1.1:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-rcppprogress", type=("build", "run"))