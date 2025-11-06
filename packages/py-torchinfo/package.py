# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTorchinfo(PythonPackage):
    """Model summary in PyTorch, based off of the original
    torchsummary."""

    homepage = "https://github.com/tyleryep/torchinfo"
    pypi = "torchinfo/torchinfo-1.8.0-py3-none-any.whl"

    # Torchinfo is MIT licensed
    license("MIT")

    version("0.0.1", sha256="2eda85821ca930d3907d2616e0defff893245e149c2ae6db00bad21740d04e02", expand=False, url="https://files.pythonhosted.org/packages/f2/cf/a3c38a82dd560d9eabd40cbd398c13917703dd676cba28927f2967938cf8/torchinfo-0.0.1-py3-none-any.whl")
    version("0.0.2", sha256="da4c04f115253dbd324fa9fbf4dfb9353b80b07d2a4587151528f1a65d57e338", expand=False, url="https://files.pythonhosted.org/packages/29/b5/0e2763af01ebb16d400b1ac152fc60bc37f2a84d327dac482061158f4414/torchinfo-0.0.2-py3-none-any.whl")
    version("0.0.3", sha256="00d2590cc578a9dd133cbd40feab9f37d716394669a5b87602f285a38ab701fb", expand=False, url="https://files.pythonhosted.org/packages/c5/a8/30bf8f968cc98a82c7cb5f0bbc536bdc0c1f740c6cac97940e0f1ff03dc1/torchinfo-0.0.3-py3-none-any.whl")
    version("0.0.4", sha256="11eb05a22927ea9b6b8dd289862f05ee0d3415c5bd9a00b5f125178c34b48d1a", expand=False, url="https://files.pythonhosted.org/packages/85/f5/4045456d028d89ccd0b856331e74024ed55e21393a2c0007237ad866b399/torchinfo-0.0.4-py3-none-any.whl")
    version("0.0.5", sha256="caa878b7d60606c64802be044a868f07853c68147c20b7c2526c6661137b5d6b", expand=False, url="https://files.pythonhosted.org/packages/bc/e1/c9e2780c7538f1e5f104d4e32817cca8e9771ec1033327d11f6011ead5c7/torchinfo-0.0.5-py3-none-any.whl")
    version("0.0.6", sha256="6d07bdb4d0049ef11816fb0bfaf5ecba4f508b2dd052935746ef5f789477c45c", expand=False, url="https://files.pythonhosted.org/packages/d3/19/0613d4e4f1b39c84a98b6ef56d453b07f8888bd8524fce7e2463cfb62e5a/torchinfo-0.0.6-py3-none-any.whl")
    version("0.0.7", sha256="fa5b2508ae967b18935865091e033ebc8c7b209693933f25a124c1e7d7d2f139", expand=False, url="https://files.pythonhosted.org/packages/11/5b/ceaddd80688baed8b03e3fb824f1ba895600496bd8f86de81030d20fd6d6/torchinfo-0.0.7-py3-none-any.whl")
    version("0.0.8", sha256="15e3f71e38cae4ad5dac1a9a0fd9639990028c5f7d36386d99e9379af36fd7fe", expand=False, url="https://files.pythonhosted.org/packages/4f/b1/4b310bd715885636e7174b4b52817202fff0ae3609ca2bfb17f28e33e0a1/torchinfo-0.0.8-py3-none-any.whl")
    version("0.0.9", sha256="b037fbff3a4554bc3afc32d7baab5e60a4910d10f0f650bb9a811375ab0c530f", expand=False, url="https://files.pythonhosted.org/packages/58/de/c2bb79cd6bb57e63feed501943cf55a197f25ae25f883ec19901843e466b/torchinfo-0.0.9-py3-none-any.whl")
    version("0.1.0", sha256="01be18d462abc1655a9633757480e6c9187750e553e04f71fc69ac4f08488ea5", expand=False, url="https://files.pythonhosted.org/packages/45/b3/c4a805dd20422136c98b2ca5e9e47c1e285d54ce9e8e3c219c6574aee0dc/torchinfo-0.1.0-py3-none-any.whl")
    version("0.1.1", sha256="e3cd3b55a2583f0663a99afc93ed8289d44a70cc3d8f19b920b61973618fb4f2", expand=False, url="https://files.pythonhosted.org/packages/00/ac/a33b67c628df213260fb0c39590dc68291382d1f66bfb159e4af27f25ca7/torchinfo-0.1.1-py3-none-any.whl")
    version("0.1.2", sha256="6f4e851a76deef16a2cdd95bacaf42453a914c021618fe14b0c6b1b480b8d5cc", expand=False, url="https://files.pythonhosted.org/packages/5f/a6/7339896cf79ee7fb244777375ee4500f881a9b4b951113aa7f6edbc8e1b2/torchinfo-0.1.2-py3-none-any.whl")
    version("0.1.3", sha256="367e781d0bac8786e45d970e8b1efbcfbf8698db53c15900c9e20bd7f87e45ec", expand=False, url="https://files.pythonhosted.org/packages/85/8d/153dc4096d2a64e1324af5fd17d3a2a19ab8051bc1e4ce375276bc0fc341/torchinfo-0.1.3-py3-none-any.whl")
    version("0.1.4", sha256="6d049a16bff2e1b9309820f437f56085ea0cef0521f937974123b01aa9cab57b", expand=False, url="https://files.pythonhosted.org/packages/ef/08/4448486fd0ae1adb086217294a626474bd221b30e32b71f40f3f7de50348/torchinfo-0.1.4-py3-none-any.whl")
    version("0.1.5", sha256="bd5205f4cf3f3c8969a7562fc150548adcd835aa9b0c8b3eda8368fe99d097f1", expand=False, url="https://files.pythonhosted.org/packages/e7/d3/11f9901d75f4d105b2b1700c81f83579fd33c4cf0ec88bb7a165d96c7bb4/torchinfo-0.1.5-py3-none-any.whl")
    version("1.5.0", sha256="69e76209af9130a1a03cfc7ad1ed0f0ef56f3f7a0685877409b07b9ce6c5dcbc", expand=False, url="https://files.pythonhosted.org/packages/e5/cf/dbc2fc569d95f5a5fca80c45afcaf2788194573f7bc4561050148a2a96d2/torchinfo-1.5.0-py3-none-any.whl")
    version("1.5.1", sha256="75f028430a0075d03172e7f2555fdd3a2bbb4cd87322a45179a739dd1b4320d8", expand=False, url="https://files.pythonhosted.org/packages/3e/d0/23b0ca143791486bee98a5afa1f64fa4b03ab7532b45a8a2a6cd5a162876/torchinfo-1.5.1-py3-none-any.whl")
    version("1.5.2", sha256="fb72d084ade00b431cb1cbd49a4921b317e764a61ad9004b83e4f06db29d0012", expand=False, url="https://files.pythonhosted.org/packages/86/3f/1ca9c336e489b2b7ae3f8cc8a361940ce67ffafc184bda0c3e0dc761eaae/torchinfo-1.5.2-py3-none-any.whl")
    version("1.5.3", sha256="46ec87260016b70e548e57dcb4a9cc40878c83ab3532fe6a3d6c60437a1ce58f", expand=False, url="https://files.pythonhosted.org/packages/36/81/4f56f2be3e6cd9180117c23b0668adb655e4c4ea106f803b31e3941926e2/torchinfo-1.5.3-py3-none-any.whl")
    version("1.5.4", sha256="b24cd9e70b10d2c04beac7eec8c7c8ba32be26c8db1a8fed776a8e0f9c6026b6", expand=False, url="https://files.pythonhosted.org/packages/b3/bc/d43629e0b4d364d04bfbcbf55fbe1218aa09b2f944eae6a4d96045bf2d0f/torchinfo-1.5.4-py3-none-any.whl")
    version("1.6.0", sha256="ddab7db843a9a4c7002122011d3cca511413665bfe1efe75004b5ba6ce23ed12", expand=False, url="https://files.pythonhosted.org/packages/5d/0a/4570e8e967caadf6cf2bea0d4d5c9897ca6e163212129a6811e62d8445c3/torchinfo-1.6.0-py3-none-any.whl")
    version("1.6.1", sha256="12c587f7131e9dc4c44ce6b08d885c80fcfb71a900586eff768bd3e266476ca9", expand=False, url="https://files.pythonhosted.org/packages/0b/50/6a76c061a76bccf437b921883f46d7a428c878cbf6c3f6254bd9dc8b1a63/torchinfo-1.6.1-py3-none-any.whl")
    version("1.6.2", sha256="8847bc7c987a6a4e8e09b65390be6af8a75216a7d48ef4af19a80c3c189f7ff0", expand=False, url="https://files.pythonhosted.org/packages/92/8a/9584a4d4c3fb48bf55174c1dfc25f1f2c30811174da79f3427b6d67d2195/torchinfo-1.6.2-py3-none-any.whl")
    version("1.6.3", sha256="5240f420d35902556ba2988b4b3d08ec3dd439bafd90e03f22d73718858dede1", expand=False, url="https://files.pythonhosted.org/packages/19/da/9d0d2cf6094c56dc9f75e9c2beb065443efc5f998bcf485e128273525ee7/torchinfo-1.6.3-py3-none-any.whl")
    version("1.6.4", sha256="fff1d7b4489fa8603ebdf6d4b52d00d5770c8b5652108bfe26782358d587a69f", expand=False, url="https://files.pythonhosted.org/packages/39/79/e1fb01712c77a385813cf4f00d1a6691b5d8692b65300c689c5534dd1833/torchinfo-1.6.4-py3-none-any.whl")
    version("1.6.5", sha256="3eaf4830342affc23c8c5e9242c1882b2ec0216190d49f1e61fc5de99ea0d059", expand=False, url="https://files.pythonhosted.org/packages/d4/f6/418ce8669c080b87cf223ff61e4b7ec07f55cedca4c8036779fc5791fe9f/torchinfo-1.6.5-py3-none-any.whl")
    version("1.6.6", sha256="406965434fd768e1ef5c373be6e73fc0e91b0f54a8818165b46297bfc493a8ad", expand=False, url="https://files.pythonhosted.org/packages/a6/c6/ed3969f4935a898c4ad9884724e91d1e86b4ca7a034da896ecd77eeb24e6/torchinfo-1.6.6-py3-none-any.whl")
    version("1.7.0", sha256="23d8771d965e50cdd242327ea4669b20978db0235da46ad7889be1b321598fea", expand=False, url="https://files.pythonhosted.org/packages/3b/b8/f5b9770c34189cb633bf3caed3575356dcc64c315dcd00a8a6c952a70deb/torchinfo-1.7.0-py3-none-any.whl")
    version("1.7.1", sha256="792d429d87814aa9ddfb0f1b9d8c75861edc6099c5d753148064d3217128ff42", expand=False, url="https://files.pythonhosted.org/packages/e6/a3/1a7647749a6c96edf8e97669586022b22fecbc471fe7823d720ce67975d4/torchinfo-1.7.1-py3-none-any.whl")
    version("1.7.2", sha256="3966557b1ab91e61dfeaa0a6c32a8f70e56819bf186da6ed347d28e14e405469", expand=False, url="https://files.pythonhosted.org/packages/89/b9/24371b25084b9368650703ecfd652669705dbf797df6e1d2c7dcc9146c15/torchinfo-1.7.2-py3-none-any.whl")
    version("1.8.0", sha256="2e911c2918603f945c26ff21a3a838d12709223dc4ccf243407bce8b6e897b46", expand=False, url="https://files.pythonhosted.org/packages/72/25/973bd6128381951b23cdcd8a9870c6dcfc5606cb864df8eabd82e529f9c1/torchinfo-1.8.0-py3-none-any.whl")

    depends_on("py-setuptools", type=("build",))
    depends_on("python@3.7:", type=("build", "run"))
    # torch is a runtime requirement
    depends_on("py-torch", type=("run",))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import torchinfo")
