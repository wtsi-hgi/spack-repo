# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySchemdraw(UvPackage):
    homepage = "https://schemdraw.readthedocs.io"
    import_modules = ["schemdraw"]
    _pypi_package = "schemdraw"

    version("0.21", sha256="b5bee2fa63e7a876dfd7478bcc7131325ead2bf7769056ee3e7873a57d799bd5", expand=False, url="https://files.pythonhosted.org/packages/fb/24/3333ee8006a466b0918cdaf3e4770df6b8a4d03965d8f43156bff493e1ef/schemdraw-0.21-py3-none-any.whl")
    version("0.20", sha256="ed750908232b25037759ff183e010f63c7b40b254da2f1e540ebae3fd1c0d995", expand=False, url="https://files.pythonhosted.org/packages/dc/a5/2916a969b80940dcaec71615bedeade23dd1871c9d57f96df582bbc7ded1/schemdraw-0.20-py3-none-any.whl")
    version("0.19", sha256="a5bc8a6af02dd8dc8225864508aca2d7950159fe2f35c8b0c0ac6bc40e3c8ba9", expand=False, url="https://files.pythonhosted.org/packages/f3/8f/aa69d21ffc0b3fc9463b369f6857118ae719d1fb011fb7e7d37cb2d89f1f/schemdraw-0.19-py3-none-any.whl")
    version("0.18", sha256="9f1957015f46118d2dfeac9d7b221032d373ac2088c8ce5ea5be726880467444", expand=False, url="https://files.pythonhosted.org/packages/90/92/f593c55bee70f200ed95c24edc7998d225b5a81181a56d267cfbc7965a93/schemdraw-0.18-py3-none-any.whl")
    version("0.17", sha256="08468b4d16c6ef6a85c6979a754cb3b528a82f43cc531819158c47e65612e619", expand=False, url="https://files.pythonhosted.org/packages/c5/41/47934c318a86769fea03e3c83dc24757c85218d5b2dd8e879f9959787553/schemdraw-0.17-py3-none-any.whl")
    version("0.16", sha256="7fab7d77b25df5b2616f1c7d9f6429eca91468d7086599401721ee1aced5a59b", expand=False, url="https://files.pythonhosted.org/packages/84/2d/941c6e496ec8e66e5a64ac03a69f9db363408d8d9de1fcb609dc38f59afb/schemdraw-0.16-py3-none-any.whl")
    version("0.15", sha256="b335ff576002d287a43701b8bc325460dbdf2d5c3522ad1894877d0e44280343", expand=False, url="https://files.pythonhosted.org/packages/8f/28/8b59385b5b4d89ba9a5710bd5d014e8fdc7823d66e15cb6f867bb0c59adc/schemdraw-0.15-py3-none-any.whl")
    version("0.14", sha256="ea8658f18f1a1de4f064a1842867e0f2467ea7116b0dfe8d04a8da05da89b16a", expand=False, url="https://files.pythonhosted.org/packages/52/05/4455fbffb5b581d1bd5cc8ee91045d0cea0a6f505a67fbd233d093d47b47/schemdraw-0.14-py3-none-any.whl")
    version("0.13", sha256="cda3dafeb328cd61544bb4c64f6d7d41774c736072eadd845676f0a2ea6b3ab8", expand=False, url="https://files.pythonhosted.org/packages/b2/e3/4778d2a4e3a26d939009347f143a49333451419091cfc8e11f15a466d41e/schemdraw-0.13-py3-none-any.whl")
    version("0.12", sha256="08b2d15d58b8a0423c89168bf7630bae9287bae48bcae0a4534326425a7a24c9", expand=False, url="https://files.pythonhosted.org/packages/5a/6d/947c15ce62c5b82f2ab6b54b80382b7f50ad2ce777d43ad9ded3b423890b/schemdraw-0.12-py3-none-any.whl")
    version("0.11", sha256="98d31c414cecf9964f1752e74be4d956e7a5d2ff459b18c761fc33ec2ad3f829", expand=False, url="https://files.pythonhosted.org/packages/b2/83/873bfe709355c11b6b4b9fa0bc8b02df59453b08cb444a85f22af9d40d99/schemdraw-0.11-py3-none-any.whl")
    version("0.10", sha256="b4da6606e4b6fd2eed9a0e393a7aade8cf57e6297a2cb0743ffcb4d3bbf4e60c", expand=False, url="https://files.pythonhosted.org/packages/38/2e/25c7bb7b9138932158a78bd2d99dab46291917da5ef0ae862d3357224d42/schemdraw-0.10-py3-none-any.whl")
    version("0.9.1", sha256="d5759c2aa60ac493d4da014a9e0efcab934178d2632cdab97f957834bbb66b6f", expand=False, url="https://files.pythonhosted.org/packages/1a/43/41d2bc4d6e5f8023d1bc5a5a1381e60bfe13be2ab3240ca28df717479d9f/schemdraw-0.9.1-py3-none-any.whl")
    version("0.9", sha256="40f5f0dfe8480d7480f759e9974bde8fb5b83febdce76362bf8930ff45bfcc95", expand=False, url="https://files.pythonhosted.org/packages/4f/36/a6ee71bd2dbb4fb7cf8f8e700db05e65fb247a7b53ec9e41a26b93a999a8/schemdraw-0.9-py3-none-any.whl")
    version("0.8", sha256="f931729388fff84d7a1ddc78f005578070a493767f65317838a728aaf201f7c0", expand=False, url="https://files.pythonhosted.org/packages/87/c2/c64538e9213b7927da7cd797e3b77a32ddfb69c094b3c32eeac605f1e900/schemdraw-0.8-py3-none-any.whl")
    version("0.7.1", sha256="05da0ea4a47c5646ccb65e4b8debd20ec7350d5c460d01c614396d9fc6005f68", expand=False, url="https://files.pythonhosted.org/packages/68/2e/95ff432d81126fcf092f160a5c4fc675e5d546c346f665ce6a970fc2e2aa/SchemDraw-0.7.1-py3-none-any.whl")
    version("0.7", sha256="ce05b248738ae0730d9501e5d25ff493902adc774a90c28d4bc83fc2737220b6", expand=False, url="https://files.pythonhosted.org/packages/1d/92/981378104526014e1f2d7488c8caa11540638ddf81e967f419a4acf2175a/SchemDraw-0.7-py3-none-any.whl")
    version("0.6.0", sha256="987429cd4e61271381113c513dd1966b1e3fb7be5c16bb32dcc3505004c6fd5c", expand=False, url="https://files.pythonhosted.org/packages/46/74/08e4c1ac0652bd1043ba6b1cca7ec3be82936de46032b20526080970a935/SchemDraw-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="0518a8182669156f344b8ce77b342d7628d97eee72bc6231137dfa2127d5c9b5", expand=False, url="https://files.pythonhosted.org/packages/a9/3e/3052082d0c3f34b0ba8e03df6f58b701be3216efcacf17c5ddb31ed98fd8/SchemDraw-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="6b85ab7341a77d935464110b5a1821f410a6f904920dd2aa6c9bc63acc0b8676", expand=False, url="https://files.pythonhosted.org/packages/03/4d/8b71e73f066b7b1686dbec08e6ef2f5fef00b5861116f31137974315aeb5/SchemDraw-0.4.0-py3-none-any.whl")
    version("0.3.1a0", sha256="a1677610c5c1e4aa5fada3e7080b67d4c94af126b9530332e2ef72884574f239", url="https://files.pythonhosted.org/packages/25/68/3926633c99a39ff9feafd67f39528092c72d69686b9f3e9421ba44c42d6f/SchemDraw-0.3.1a0.tar.gz")
    version("0.3.1", sha256="78a6f203af49996596a0a240c7f40539720286627284753a6b7e9794dd7613d0", url="https://files.pythonhosted.org/packages/02/d7/2573f796f21eacb939a1fb0b270d43d70d5a6e2177e7d8805cdb4ae3fc48/SchemDraw-0.3.1.tar.gz")
    version("0.3.0", sha256="0aa1deed959b61cf129d02fe2470e1e3831e836646e5e58c0d036e3e573821ea", url="https://files.pythonhosted.org/packages/23/19/d9765c4036ac5f60e687429f3531320b19c2ae7348f52b3f291609a1f732/SchemDraw-0.3.0.tar.gz")
    version("0.2.2", sha256="388b0e7d8df1aaeb712c23192622f8658d911f60b4b5ce2399863def0e868191", url="https://files.pythonhosted.org/packages/fe/49/39e7157e5434dbea18ff6c5b6a5002da4c15d3c643d1b2f49154c3d806f9/SchemDraw-0.2.2.tar.gz")
    version("0.2.1", sha256="9968709e63bab0540bf9b960c700c58b8b0498b36a868a6a43ab223fb0925400", url="https://files.pythonhosted.org/packages/91/12/03818f9d50fe65799870de029fa0ee6ff3b5bbe3a1851e6d62b62e5bcd0d/SchemDraw-0.2.1.tar.gz")
    version("0.2.0", sha256="614f7e0e84633e5b1021609423a014058c5307689636b35b1d1bbc20dd23f0cd", url="https://files.pythonhosted.org/packages/33/97/9ccb0a0662830ca102d2dbe80b3c43ebd77b2aa5cb9c57917e0f2a19e198/SchemDraw-0.2.0.tar.gz")
    version("0.1.4", sha256="5fce4b5e6f1f1f164790a53174e4f3837ae12640cf0df29ef3e34e75e4a2ecd8", url="https://files.pythonhosted.org/packages/fb/06/306ee7ea316d2bd8937399667ad17b6e8b5e64a6252d03995a1ac2b982e4/SchemDraw-0.1.4.tar.gz")
    version("0.1.3", sha256="0ac7fa47f953d1abe6a5f8fa82e804934d6aec5e2c416ca8ce2bcf2c292341cf", url="https://files.pythonhosted.org/packages/3d/4f/059725d663bc35c441b701896e46827c22fc9a70ff562574503de6229a29/SchemDraw-0.1.3.tar.gz")
    version("0.1.2", sha256="8337c7e913dd6b3464f07d2c7d25627840bb41bdaa2c0a304a243e27b6757fb9", url="https://files.pythonhosted.org/packages/01/e3/4a35887a24d7bb6e491a2b02fba1afa4eac5b133674be0a93718b0044bb7/SchemDraw-0.1.2.tar.gz")
    version("0.1.1", sha256="5b17eaae3f63d22c59622a929fd2347f4329d263023afdacb9a90e7414cf717b", url="https://files.pythonhosted.org/packages/fb/49/90d4841b21843404523bff5e991cdce40cee690d22cca937693f6530b2ab/SchemDraw-0.1.1.tar.gz")
    version("0.1.0", sha256="8429a2c8d73539c1280dda144d427429fe09cd592de7f97edbc042bf95d64537", url="https://files.pythonhosted.org/packages/29/9d/d8ed4c4c3e3ff1ce3bba8c22fd444d7807d4e6e8cac8487088f3b7ddd9d9/SchemDraw-0.1.0.tar.gz")


    depends_on("python@3.9:", type=("build", "run"), when="@0.21")
    depends_on("python@3.8:", type=("build", "run"), when="@0.20")
    depends_on("python@3.8:", type=("build", "run"), when="@0.19")
    depends_on("python@3.8:", type=("build", "run"), when="@0.18")
    depends_on("python@3.8:", type=("build", "run"), when="@0.17")
    depends_on("python@3.8:", type=("build", "run"), when="@0.16")
    depends_on("python@3.7:", type=("build", "run"), when="@0.15")
    depends_on("python@3.7:", type=("build", "run"), when="@0.14")
    depends_on("python@3.7:", type=("build", "run"), when="@0.13")
    depends_on("python@3.7:", type=("build", "run"), when="@0.12")
    depends_on("python@3.7:", type=("build", "run"), when="@0.11")
    depends_on("python@3.7:", type=("build", "run"), when="@0.10")
    depends_on("python@3.7:", type=("build", "run"), when="@0.9.1")
    depends_on("python@3.7:", type=("build", "run"), when="@0.9")
    depends_on("python@3.7:", type=("build", "run"), when="@0.8")
    depends_on("python@3.7:", type=("build", "run"), when="@0.7.1")
    depends_on("python@3.7:", type=("build", "run"), when="@0.7")
    depends_on("python@3:", type=("build", "run"), when="@0.6.0")
    depends_on("python@3:", type=("build", "run"), when="@0.5.0")
    depends_on("python@3:", type=("build", "run"), when="@0.4.0")
    
    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import schemdraw")
