# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyImmunebuilder(PythonPackage):
    """Set of functions to predict the structure of immune receptor proteins"""

    homepage = "https://pypi.org/project/ImmuneBuilder/"
    # Prefer building from source tarballs
    pypi = "immunebuilder/immunebuilder-1.2.tar.gz"

    license("BSD-3-Clause")

    # Source distributions with verified checksums
    version("1.2", sha256="18562dcabc3733e0ce47a9782e73cc0a7f1a876f266e73b5d59872c64374586d")
    version(
        "1.1.1",
        sha256="0045cf87e583356a01cae9fd015d5d2da3e9e3de5c79bd4c34bf9926eadb066c",
        url="https://files.pythonhosted.org/packages/9e/16/6e54cee4269758c3143f2eae8eb5f1bc79684c6e90aa843f5c60343285e0/immunebuilder-1.1.1.tar.gz",
    )
    version(
        "1.0.1",
        sha256="6099742debdd92edde204d595279f74741e65365f01c7dd81c40b2d271340bc9",
        url="https://files.pythonhosted.org/packages/af/e2/703397ee6569f9490a6b023fb561c76791ce96d8d01819b3638e4bbb4322/ImmuneBuilder-1.0.1.tar.gz",
    )
    version(
        "1.0.0",
        sha256="814a387c0f08491816bb5c3b4a0a63fff66881dc900f2dcefca5b5d02ea6e4f3",
        url="https://files.pythonhosted.org/packages/c4/5a/cf6f2b45429d404ad5ce6c3d98afd2d460982e4093d78b6bf7f1d621181f/ImmuneBuilder-1.0.0.tar.gz",
    )
    version(
        "0.0.9",
        sha256="403b8dbcc552bbdb8c82b98629b7ab13fffbf0434ba0ed895cef1c938b3e6362",
        url="https://files.pythonhosted.org/packages/a7/1a/fbb2cda814f30c92d36e9d522cf6aeecf929fc20b8990874c4afcd9c0581/ImmuneBuilder-0.0.9.tar.gz",
    )
    version(
        "0.0.8",
        sha256="18ca19309a4f3a0f7369785d0ecd714759e99d0876dc94ecba4be6a7a8512d99",
        url="https://files.pythonhosted.org/packages/d7/fc/d8cf7e599cbff74caabde2fe36a1baf6d87568fe259870604e9f4cb4503b/ImmuneBuilder-0.0.8.tar.gz",
    )
    version(
        "0.0.7",
        sha256="36c43042336d0877ee189c9dbac3954df52794dcc9617fc3596f25c483ef9027",
        url="https://files.pythonhosted.org/packages/48/6f/37a4ce9515bc3e09728ee1e7b60b16de96b8a18aaf1a363b45f6d8871a9c/ImmuneBuilder-0.0.7.tar.gz",
    )
    version(
        "0.0.6",
        sha256="239d2f974918bc85429f6c7dddc6112602cafa2ebd3b18e2402504b8ec83257a",
        url="https://files.pythonhosted.org/packages/d6/49/4bd7b45fa9c8eda204f2e42439cb65dfef955dbb5f31f38dd2321bb7cb82/ImmuneBuilder-0.0.6.tar.gz",
    )
    version(
        "0.0.5",
        sha256="4ebebeb6792adc6fdac80fee0fec2a813185d98de6241a96bf7119a9d7dcb517",
        url="https://files.pythonhosted.org/packages/35/66/6e6343d51bcf15256172bcc7fb963629e76fd192c60065444674b9dde2f3/ImmuneBuilder-0.0.5.tar.gz",
    )
    version(
        "0.0.4",
        sha256="8f1508a2eed999f82f7c3a60ed37ff810878774739b78bdaac2ee2f59d7425e8",
        url="https://files.pythonhosted.org/packages/f8/22/dce7ffded153ca4d8678f0113c30067b9242e64ee0da7519561ee68643ac/ImmuneBuilder-0.0.4.tar.gz",
    )
    version(
        "0.0.3",
        sha256="ddf52dbcbff2327abef847c52ea41c2559067443415998e6b9d9a4319f4eb3e4",
        url="https://files.pythonhosted.org/packages/90/36/fa736209f45841978ca31c2cb6567eebc2107e2e348fe3090bbe28eb7ab2/ImmuneBuilder-0.0.3.tar.gz",
    )
    version(
        "0.0.1",
        sha256="197c885aefd0d5f00a00a6bb4b10a17334cf1aaee6ec86ba8537d777c0930a10",
        url="https://files.pythonhosted.org/packages/5b/62/c90966963cfe975012a477b77393d89ff2e1e0ea1ed99085b154de7ab254/ImmuneBuilder-0.0.1.tar.gz",
    )

    depends_on("python@3.9:3.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-scipy@1.6:", type=("build", "run"))
    depends_on("py-einops@0.3:", type=("build", "run"))
    depends_on("py-torch@1.8:", type=("build", "run"))
    # Required at import time via ImmuneBuilder.refine -> pdbfixer
    depends_on("py-pdbfixer", type=("build", "run"))
    # Required at import time via ImmuneBuilder.sequence_checks -> anarci
    depends_on("py-anarci", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # No CLI; basic import test
            python("-c", "import ImmuneBuilder")
