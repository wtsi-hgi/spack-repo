# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFirthlogist(PythonPackage):
    """Python implementation of Logistic Regression with Firth's bias reduction"""

    homepage = "https://github.com/jzluo/firthlogist"
    pypi = "firthlogist/firthlogist-0.5.0-py3-none-any.whl"

    version("0.0.2", sha256="42d9872f6971e7bb46347476d883f6bb99349ff2b77386e9ccd836045e969c31", expand=False, url="https://files.pythonhosted.org/packages/a5/b0/5c1ee7ad4709595a54bf90f9730d61c1c4164545cf163505e99ece25fe91/firthlogist-0.0.2-py3-none-any.whl")
    version("0.0.3", sha256="b5fdccea9acd7c8a9e07db882d49ffffed7033e13f6d8eedfa2b14341f4b1723", expand=False, url="https://files.pythonhosted.org/packages/75/78/0beaae79d824fbd2ddf18ee0493156d03c8d50f837a33c698062e215231d/firthlogist-0.0.3-py3-none-any.whl")
    version("0.0.4", sha256="ab05f77d5bd9ae9de9ee5a0ced1a2bbb46b8f41b3019fb0a8b0d3dc6de705b69", expand=False, url="https://files.pythonhosted.org/packages/4c/4e/073b4d8afc7a02a4f35a1cd403ebc77c6593f2eef6c0e5a06c762a15e1c7/firthlogist-0.0.4-py3-none-any.whl")
    version("0.1.0", sha256="0e9eee1cb63e129f5a534f6872ab3042fe8da12d8bce07d2c345e10c959b35c1", expand=False, url="https://files.pythonhosted.org/packages/df/be/8ff660e4e2739826289c9d4a51d6a14538736a7ec23d926f2eee299c2cbf/firthlogist-0.1.0-py3-none-any.whl")
    version("0.1.1", sha256="e5e2fb3b01ca44bf402565359a78058312b23662ef50facc9985801c5f690505", expand=False, url="https://files.pythonhosted.org/packages/b2/d3/06202a65d6706d1f25badf40dd43ab4b9c4697402dfc350d4d0cd0948de5/firthlogist-0.1.1-py3-none-any.whl")
    version("0.1.2", sha256="2d777db68c8a535721c03eaca05b2312cf5b2b51e5c34f6feeff77ea72dbd144", expand=False, url="https://files.pythonhosted.org/packages/a6/09/f9236abbfaf34fcc476a9711fd85b54a633193224f9c55ba8b9fede7d305/firthlogist-0.1.2-py3-none-any.whl")
    version("0.2.0", sha256="3e2309e997d013e4001779c9dbc173bb6ffd1995b993f7c9c93eeb77e64fd736", expand=False, url="https://files.pythonhosted.org/packages/28/31/0c65e00a26144f824a177416d18657d8f2320fc3cd207f885228325e5701/firthlogist-0.2.0-py3-none-any.whl")
    version("0.3.0", sha256="690554188640084aa274d85dbcb239125e7abf502062739a445c8534b18742ab", expand=False, url="https://files.pythonhosted.org/packages/0d/09/f748822fe112a70a23db56d309d0cdd74653bdda28617c3e03c0d47b73ea/firthlogist-0.3.0-py3-none-any.whl")
    version("0.3.1", sha256="288e7250fa83fd98a576d997bec6dea2e87a278c9ee6c1e15060f72c05936891", expand=False, url="https://files.pythonhosted.org/packages/79/59/17ced137e9e34d5b86d04532d007c09cc6edcfb5a7d0f476de2a2662311b/firthlogist-0.3.1-py3-none-any.whl")
    version("0.4.0", sha256="e383f609b1c2fee513c61cffe888794386c6d5778157383689d26941e9badc06", expand=False, url="https://files.pythonhosted.org/packages/1f/da/fff97963ae0abdd370175c87daa9cdbce160a31ba0fedbe38bd87a269cb4/firthlogist-0.4.0-py3-none-any.whl")
    version("0.5.0", sha256="9a38bf9ba18fa0e19991380d6518b796186af4209e5e349e9b42052e5d25ff62", expand=False, url="https://files.pythonhosted.org/packages/7f/1f/112d1269f0f1482d10e44cd3edc37857376284539cc13790b69d13b25833/firthlogist-0.5.0-py3-none-any.whl")

    depends_on("python@3.8:3.10", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.22.4:1", type=("build", "run"))
    depends_on("py-scikit-learn@1.1.1:1", type=("build", "run"))
    depends_on("py-pandas@1.4.2:1", when="@:0.1.2", type=("build", "run"))
    depends_on("py-tabulate@0.8.10:0.8", when="@0.3.0:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import firthlogist")
