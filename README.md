<img width="1439" alt="ethdenver-2022-header" src="https://user-images.githubusercontent.com/149245/151204295-840df036-c96b-4723-8943-42a73c1bf4a0.png">

# VEGA ETHDenver Virtual Hackathon Launchpad

### Thinking of participating in the ETHDenver 2022 virtual hackathon and working on one of the Vega bounties? Well, you're in the right place. The launchpad gives detailed information on each of the bounty challenges, the project, sample code and more.


## What is Vega?

Vega Protocol is software that provides a proof of stake blockchain for creating and trading derivatives. It provides infrastructure for decentralised markets that settle in assets held on Ethereum and other major collateral blockchains. Vega facilitates high speed, permissionless derivatives markets. 

Why derivatives? Because they are an essential class of instruments for any financial system as they allow risk to be partitioned across time and market participants bringing more stability to those who seek it and additional investment opportunities for others. We’re hoping that it will allow DeFi to fully blossom and reach unprecedented levels of adoption.

Through a rich set of APIs, developers can build on top of Vega. Platform engineers can plug into trading data and order flow with CEX-like ease. Front-end hackers can create immersive web, mobile or desktop applications rich with real-time data, for example Vega Console: A Javascript application built with React which makes heavy use of the GraphQL API.

Vega believes that the web3 community can help build the future of DEFI derivatives. We're super excited to see what you come up with during the hackathon.

## Judging Criteria


### The In-Person hackathon has ended, but the virtual hackathon continues to 20th March 2022 :) Anyone can participate! <a href="#how-to-submit-your-entry">How do I submit my entry?</a>

This year at ETH Denver, we'll be judging bounties with the following criteria:

* **Creativity and user experience**
* **Learning and understanding of Vega**
* **Technicality and coding style**
* **Completeness and delivery of features given in the brief**

Note: Each bounty brief also contains a list of more detailed pointers to help guide you towards the ideal solution we're looking for - look out for 'Bounty Criteria' at the bottom of each brief. All prizes are mirrored 50/50 between in-person and virtual hackathons (as shown).

### Happy Buidling!

## Our Bounties

# 1 - Build a Vega block explorer

### PRIZES:<br>VIRTUAL **$2500** USDT (winner)  **$1250** USDT (runner-up)<br>IN-PERSON **$2500** USDT (winner)  **$1250** USDT (runner-up)

Bounty awards will go to the best teams that create (or extend) a block explorer to report and visualise blockchain transaction data as well as any Vega state changes queried from a data node.

Vega networks run on a proof-of-stake blockchain powered by Tendermint, connected by ABCI to a custom high-performance trading core application, this is additionally supported by data APIs (data nodes) to retrieve state information by gRPC, REST and GraphQL.

The goal for this bounty is to build a visual, web based, block explorer that shows the transaction data in the Tendermint blocks, state of the blockchain, as well as Vega state changes resulting from transactions. This may include but is not limited to: trades, orders, deposits, withdrawals, etc.

The solution should be open source and easy to demonstrate in a web browser, with a walkthrough video showing all features implemented. The solution needs to show both Vega and Tendermint data. Installation instructions must be given. Extra points awarded for having a roadmap showing scope for future work. 

See the section [Bounty Criteria](#bounty-criteria) below for the tasks and features we're hoping you can try and deliver for this bounty brief.

#### WHAT IS A BLOCK EXPLORER?

A block explorer is a tool to view information on all transactions that have taken place on a blockchain. Typically a block explorer will show key information about the chain, for example, the current network hash rate, validator statistics, activity on blockchain addresses and other useful information. You can think of it as a window into the blockchain world, giving you the opportunity to observe what’s happening on it - live and in near real time. Popular Ethereum block explorers include Etherscan, Etherchain and blockscout. 

For Vega networks, all transactions and state changes should be transparent to the users of the protocol. A Vega block explorer will therefore help users track and visualise both the transactions and the output state from the operations or commands contained within transactions.

#### INSPIRATION

The Vega engineers have built a very simplistic web based implementation of a block explorer to give you inspiration, as well as a reference for decoding transactions. **Whilst fun to play with and learn from, we'd recommend starting from scratch with React or similar - rather than simply forking this repo!**

<a href="https://explorer.vega.trading"><img width="843" alt="block-explorer" src="https://user-images.githubusercontent.com/149245/152604768-69ac788c-d81f-422c-a8fa-bf57a2b071de.png"></a>

This app is built with Svelte, and uses Golang code to decode signed Vega transactions from within blocks on the Vega Fairground Testnet. Shout out to @edd and the team!

* [Vega Explorer](https://explorer.vega.trading) (hosted on Netlify, attached to Fairground)
* [Vega Explorer on GitHub](https://github.com/vegaprotocol/explorer)
 
We feel the greatest hackathon teams are often made up of multi-discipline groups, UX and UI designers can unite with code developers to create tools of beauty - and with this bounty we invite you to do just that. Please present Vega transaction data with design flair as well as consistency.

#### BOUNTY CRITERIA

In addition to the overall Judging Criteria, for this bounty, we'd love you to try and achieve the following:

* **Learning of data structures and transaction commands on Vega**
* **Report blockchain data on transactions from Tendermint**
* **Report Vega state data from data nodes, this might include:**<br/>**Markets, Orders, Trades, Accounts, Assets, Parties, Withdrawals, Deposits**
* **Validator statistics and staking information**
* **Demonstrate the web app running on the Vega testnet**
* **Write clean and understandable code**
* **Documention for the app to help future developers**
* **Roadmap for future work**

There's room for plenty of stretch goals with this bounty, dont hesitate to reach out to us on Discord or in-person to learn more.

#### LINKS & RESOURCES FOR THIS BOUNTY

* **[Vega Concepts](https://docs.vega.xyz/docs/concepts/vega-chain/)** - Important concepts to understand on Vega, from tokens to staking and delegation
* **[Fairground API documentation](https://docs.testnet.vega.xyz/docs/apis/block-decoder/)** - Tendermint and Block explorer (Block Decoder API)
* **[Fairground API how-to guides](https://docs.fairground.vega.xyz/docs/api-howtos/)** - Getting started, data node and state queries
* **[Vega API Documentation](https://docs.vega.xyz/api/overview/)** - Wallet, gRPC, GraphQL and REST documentation
* **[Vega Explorer](https://github.com/vegaprotocol/explorer)** - Supporting code repo to help understand and interact with Vega transactions, see Block Decoder. *Note: you can port this logic to your own language/app ;)* 

For more help please see the General Support & Resources section or reach out to us on our social channels.


# 2 - Visualise staking and delegation on Vega networks

### PRIZES:<br>VIRTUAL **$2500** USDT (winner)  **$1250** USDT (runner-up)<br>IN-PERSON **$2500** USDT (winner)  **$1250** USDT (runner-up)

Bounty awards will go to the teams that create the most impressive apps that can track, store and visualise staking and delegation on Vega. These tools should help the Vega community to keep the network safe and decentralised by informing others about the state of the network, as well as educating on staking fundamentals with respect to Vega.

Vega networks run on a delegated proof-of-stake blockchain powered by Tendermint, connected by ABCI to a custom high-performance trading core application, additionally supported by data APIs (data nodes). Data node APIs are used to retrieve state information by gRPC, REST and GraphQL. 

For the Fairground Testnet, there’s a minimal amount of information describing the stake held by it’s validators, as well as a mechanism to delegate stake from a wallet available at: https://token.fairground.wtf/staking 

We’re sure you can take this data further, so we are looking for a solution that is ideally a web app, with a simple yet beautiful user interface that shows the state of staking and delegation to a network of Vega validators. From a user experience and design perspective we’re hoping to see novel interactive ways to represent distribution of stake and educational information messages to help guide token holders when choosing where to delegate their stake on a network. 

The app should be open source and easy to demonstrate, extra kudos for including a walkthrough video showing all features implemented. Installation instructions must be provided.

See the section [Bounty Criteria](#bounty-criteria-1) below for the tasks and features we're hoping you can try and deliver for this bounty brief.

#### WHAT IS DELEGATED PROOF OF STAKE (DPOS)?

Delegated Proof of Stake (DPOS) protocols are often thought to be a more democratic than traditional Proof of Stake consensus designs. DPOS users are able to vote on delegates who will help to secure the network. Delegators act as the individuals within a democratic governance system who vote on electing representatives. 

Representatives are typically referred to as validators. Users can delegate tokens to nodes operated by validators in order to reduce the time and cost required for the block generation agreement.

The particular voting power of a validator is proportional to the number of tokens that have been delegated to them. In return for their help in securing the network, validators are awarded a percentage of the staking rewards earned by delegators within the network.

The number of nodes that can form a new block is smaller compared to traditional proof of stake which enables faster block creation times and overall faster transactions per second (TPS). These features are quite desirable when designing distributed financial trading systems, and therefore is currently employed within Vega.


#### INSPIRATION

There are a handful of community tools/UIs that have been built to show staking and delegation data from Vega networks, use these as help but we strongly believe you can go further with your challenge submissions:

<a href="https://stake.nodes.guru/vega/world" target="_blank"><img width="843" src="https://user-images.githubusercontent.com/149245/152829604-d1eaee6f-9dbc-4cc8-b876-7dbc8001daaa.png"></a>
**LINK:** `VEGA Staking World - Nodes.guru`

<br/>
<a href="https://ryabina.retool.com/embedded/public/9567cc8a-832e-4978-b30f-0251929fde96" target="_blank"><img width="843" src="https://user-images.githubusercontent.com/149245/152829660-62d08e29-8c51-4eea-9640-d1a9380bed9b.png"></a>

**LINK:** `VEGA Dashboard - Ryabina`

#### BOUNTY CRITERIA

In addition to the overall Judging Criteria, for this bounty, we'd love you to try and achieve the following:

* **Learning of DPOS on Vega and related APIs**
* **Design a novel user interface to show key information on staking on Vega**
* **Help the community to make informed decisions about how many tokens to nominate and to which validator***
* **Help the community to understand the potential return in tokens that they might receive from staking (given some assumptions)**
* **Help the community to understand the current state of the system (how much is staked in this epoch, versus the next epoch)**
* **Demonstrate your submission, running against a Vega network**
* **Write clean and understandable code**
* **Documention for the app to help future developers**
* **Roadmap for future work**

There's room for plenty of stretch goals with this bounty, dont hesitate to reach out to us on Discord or in-person to learn more.

#### LINKS & RESOURCES FOR THIS BOUNTY

* **[Tendermint dPOS vs EOS dPOS](https://blog.cosmos.network/consensus-compare-tendermint-bft-vs-eos-dpos-46c5bca7204b)** - Describes in more detail the concepts of Tendermint DPOS
* **[Vega Concepts](https://docs.vega.xyz/docs/concepts/vega-chain/)** - Important concepts to understand on Vega, from tokens to staking and delegation
* **[Fairground API documentation](https://docs.testnet.vega.xyz/docs/apis/)** - Information on testnet including choosing an API (if you want streaming on a front end client, go for GraphQL)
* **[Fairground API how-to guides](https://docs.fairground.vega.xyz/docs/api-howtos/)** - Getting started, data node and state queries
* **[Vega API Documentation](https://docs.vega.xyz/api/overview/)** - Wallet, gRPC, GraphQL and REST documentation
* **[Vega Token Frontend UI](https://github.com/vegaprotocol/token-frontend)** - Github repo containing the code for `https://token.fairground.wtf`, a UI/dAPP for staking and delegation (amongst other features)
* **[Vega API samples](https://github.com/vegaprotocol/sample-api-scripts)** - Collection of sample API scripts and queries to help you get started coding 
* **[How to use GitPod](https://docs.fairground.vega.xyz/docs/api-howtos/getting-started/#introducing-gitpod-to-run-code-samples)** - Experiment with Vega sample API scripts in a browser environment

For more help please see the General Support & Resources section or reach out to us on our social channels.

# 3 - Create Vega Liquidity Provision (LP) Bots

### PRIZES:<br>VIRTUAL **$2500** USDT (winner)  **$1250** USDT (runner-up)<br>IN-PERSON **$2500** USDT (winner)  **$1250** USDT (runner-up)

Liquidity Provision (LP) is on one of the central concepts of Vega. So for this challenge, winning bounty awards will go to the teams that create the most impressive LP bots (also commonly known as Market Making bots!). 

Vega aims to bring decentralised derivatives trading to anyone on earth by making market creation permissionless. There’s one gotcha though: those markets will only be truly useful if their participants can trade there with sufficient liquidity. That’s why liquidity incentives have always taken a prominent part in the design of the protocol. They are built so that markets can operate with sufficient liquidity at all times and structured in such a way that market makers should find it attractive to support even the nascent markets that haven’t been traded anywhere else yet.

After learning about the LP concepts on Vega, teams will need to research and code one or more bots following a market neutral strategy against a [specific Vega network](#important-setup-and-test-market-information) chosen by us.

The bot code should be open source and easy to demonstrate to the Vega judges. The solution needs to show good understanding of core concepts of Vega. It should be easy to differentiate between the components dealing with API integration and the market making logic. The code should be clean and well written with installation instructions provided.

See the section [Bounty Criteria](#bounty-criteria-2) below for the tasks and features we're hoping you can try and deliver for this bounty brief.

#### WHAT IS A MARKET MAKER?

Your role as a market maker will be to supply orders to both sides of the order book (buy and sell). Your orders sitting on the book earn fees as they get hit resulting in trades. You also get a portion of the liquidity fee from all trades in that market. However, your bot needs to efficiently manage it’s positions as your overall goal is to just make profit on the fees while remaining market neutral in the long run. You don’t want to amass a significant position - neither long (lots of buy orders) nor short (lots of sell orders) - as the market can always go against you in the future spoiling your hard earned fee riches.  

#### LIQUIDITY PROVISION MECHANICS

In order to become a liquidity provider for a market running on Vega an appropriate transaction needs to be submitted to the network. It consists of:

* liquidity commitment amount,
* fee bid,
* buy & sell side order shapes.

Liquidity commitment amount is denoted in the settlement currency of the market and represents the amount you are willing to set aside as an additional collateral guarantee for your orders. It gets locked in a dedicated account and cannot be removed at will. The higher the commitment, the more orders you need to provide, but also the higher the share of your liquidity fee earnings will be. 

Fee bid is your proposed liquidity fee. The higher the fee the bigger portion of each trade that goes to the liquidity reward pool, but higher fees will eventually translate to lower trading volumes so choose this wisely to maximise the liquidity rewards. 

Bear in mind that you are competing with other market makers when proposing a liquidity fee. Therefore, you should strike a balance between maximising the fee you want to earn and being competitive within the broader marketplace. You might like to query existing LP orders to see how much others have bid when deciding what your fee should be.

If at any point there isn’t enough liquidity supplied in respect to market’s demand it will go into a liquidity monitoring auction. When the market is in auction buy and sell orders are allowed to cross on the order book without trades being generated. Only once enough additional liquidity gets posted or enough parties choose to reduce their positions such an auction concludes. No trades means no fees so watching after the wellbeing of the market is in your best interest!

Trading on Vega is margined, which means that each party posting orders or maintaining position needs to post collateral. Furthermore, all markets are marked to market after every trade. That basically means that if the market moves in your favour you receive a payment, otherwise you’re out of luck and need to pay. 

All of those transactions happen between parties' margin accounts, if at any point the margin account balance drops too low the protocol will try to allocate additional funds from the party's general account. If that’s not possible their position will be liquidated and any remaining margin balances will be confiscated and placed in the market's insurance pool.

Liquidity providers are free to meet their liquidity commitment by manually maintaining orders. All their orders are weighted by the probability of trading implied by the market's risk model, so the further away from mid-price they are placed, the higher volume they need to provide to fulfil their commitment.

If at any point in time orders maintained by your bot don’t cover the liquidity commitment the order “shapes” submitted as part of the LP transaction will get automatically deployed by the protocol and their size will be calculated (and recalculated on every market move) so that the liquidity commitment is met. If your margin account balance is not sufficient to cover these orders your initial commitment amount will be used to cover the shortfall (along with a penalty which will be paid into the market's insurance pool). Should the entire commitment amount be depleted, you will get liquidated and will no longer earn any fees from the market. So do make sure to leave enough assets in your general account to support your trading! 

Splitting your funds wisely between the commitment amount and other funds to actually support orders required to meet it is another skill you have to master. 

### Don’t worry if all of this sounds rather complicated, in addition to the video guides and walk-throughs listed below, there will be an opportunity to attend the workshop [Programming Liquidity on Vega Futures Markets](https://www.eventbrite.com/e/vega-protocol-programming-liquidity-on-futures-markets-tickets-261339171497) where the Vega team will demonstrate some of these concepts to you in more detail :brain:

#### IMPORTANT SETUP AND TEST MARKET INFORMATION

Throughout the hackathon all the participants will have access to a test network running a custom futures market. You won’t be alone though, there will be various bots operating on it in order to make it more like a live market.

This market is called 'Tesla Quarterly (30 Jun 2022)' and you will need to deposit the Ropsten ERC-20 test asset tEURO to a Vega Wallet in order to place liquidity orders.

#### BOUNTY CRITERIA

In addition to the overall Judging Criteria, for this bounty, we'd love you to try and achieve the following:

* **Learning of the concepts of LP on Vega**
* **Place an LP order on the Tesla Quarterly (30 Jun 2022) market using a bot**
* **Ability to manage your LP order programmatically and update positions**
* **Implement a market-neutral market making strategy**
* **Demonstrate the code and strategy running on the Vega testnet**
* **Write clean and understandable code**

#### RELATED WORKSHOP VIDEOS

[![Watch the video](https://img.youtube.com/vi/BfbveVQpz3c/maxresdefault.jpg)](https://youtu.be/BfbveVQpz3c)
**VIDEO:** `Vega Testnet Jam - Liquidity Provision (with David Siska)`

[![Watch the video](https://img.youtube.com/vi/b8FO1rlaFqg/maxresdefault.jpg)](https://youtu.be/b8FO1rlaFqg)
**VIDEO:** `Vega Community Call #6 - Introducing Liquidity (with Barney Mannerings)`

#### RESOURCES FOR THIS BOUNTY

* **[How to sign transactions with Vega Wallet](https://github.com/vegaprotocol/vegawallet/blob/develop/service/README.md#commands)** - See also API how-to guides below
* **[How to submit liquidity provisions on Vega](https://docs.fairground.vega.xyz/docs/api-howtos/liquidity-provision/)** - Recommended example guide in Python
* **[How to deposit and withdraw ERC-20 assets on Vega](https://docs.fairground.vega.xyz/docs/console/#how-to-deposit-tokens-to-use-on-vega)** - Use Fairground Console to deposit test assets
* **[Vega Concepts](https://docs.vega.xyz/docs/concepts/vega-chain/)** - Important concepts to understand on Vega, from tokens to staking and delegation
* **[Fairground API documentation](https://docs.testnet.vega.xyz/docs/apis/)** - Information on testnet including choosing an API (if you want streaming support for your bot, go for gRPC or GraphQL)
* **[Fairground API how-to guides](https://docs.fairground.vega.xyz/docs/api-howtos/)** - Getting started, data node and state queries
* **[Vega API Documentation](https://docs.vega.xyz/api/overview/)** - Wallet, gRPC, GraphQL and REST documentation

For more help please see the General Support & Resources section or reach out to us on our social channels.


# 4 - Interact with Vega in your Favorite Spreadsheet


### PRIZES:<br>VIRTUAL **$2500** USDT (winner)  **$1250** USDT (runner-up)<br>IN-PERSON **$2500** USDT (winner)  **$1250** USDT (runner-up)

The winning award will go to the team that offers the most amazing community plugin for interacting with Vega data via a spreadsheet, you’ll be building for Google Sheets or Microsoft Excel. 

Inspired by projects like "Cryptosheets.com" and the team's general love for all things spreadsheet, the task for this bounty is to connect the Vega APIs to Google sheets or Microsoft Excel in the form of a plugin/add-in/script and provide a set of useful operations e.g. trades for public key, list of markets, place an order, etc. 

The goal is to provide simple and easy to understand visual access to data from a Vega network, with powerful features that are currently only exposed by applications like https://console.fairground.wtf or direct via API scripts.

The plugin/add-in should be open source and easy to demonstrate, with a walkthrough video and a helpful installation guide showing how to add to your spreadsheet.

See the section [Bounty Criteria](#bounty-criteria-3) below for the tasks and features we're hoping you can try and deliver for this bounty brief.

#### INSPIRATION

<img width="843" src="https://user-images.githubusercontent.com/149245/153031035-653ba29c-0bd6-4c61-a6df-5e8f9c04768e.png" />

#### BOUNTY CRITERIA

In addition to the overall Judging Criteria, for this bounty, we'd love you to try and achieve the following:

* **Learning of the concepts, APIs and design of Vega**
* **Choose either Google Sheets or Microsoft Excel as the spreadsheet client to work with.**
* **Connect to Vega's APIs (REST, gRPC or GraphQL) from the spreadsheet client in order to load and display testnet (or mainnet) data in the spreadsheet. Note: It is recommended to make the node to connect to customisable (for example, on testnet there are several geo-located API nodes).**
* <strong>Potential views/operations* to include:</strong>
  * **Markets and market data**
  * **Governance proposals and voting data**
  * **Staking and delegation data**
  * **Party (for a public key) data, including orders, positions and trades**
  * **Last n trades and last n orders on a market**
  * **Vega network statistics**
  * **Advanced: Log in to wallet and place/amend/cancel orders on a market**
  * **Advanced: Candle data / charts**
  * **Advanced: Liquidity provision (LP) data**


There's room for plenty of stretch goals with this bounty, dont hesitate to reach out to us on Discord or in-person to learn more.

#### LINKS & RESOURCES FOR THIS BOUNTY

* **[Fairground API documentation](https://docs.testnet.vega.xyz/docs/apis/)** - Information on testnet including choosing an API (if you want streaming on a front end client, go for GraphQL)
* **[Fairground API how-to guides](https://docs.fairground.vega.xyz/docs/api-howtos/)** - Getting started, data node and state queries
* **[Vega API Documentation](https://docs.vega.xyz/api/overview/)** - Wallet, gRPC, GraphQL and REST documentation
* **[Vega Console walk-through](https://youtu.be/C0_Uh8_HvDc)** - Recording/video showing how to use Console, a UI/dApp for Vega markets
* **[Vega API samples](https://github.com/vegaprotocol/sample-api-scripts)** - Collection of sample API scripts and queries to help you get started coding 
* **[How to use GitPod](https://docs.fairground.vega.xyz/docs/api-howtos/getting-started/#introducing-gitpod-to-run-code-samples)** - Experiment with Vega sample API scripts in a browser environment

For more help please see the General Support & Resources section below or reach out to us on our social channels.

# How to submit your entry

Please visit the hackerlink.io / ETHDenver 2022 Virtual Hackathon website to register your team and **[submit your BUIDL](https://hackerlink.io/hackathon/ethdenver22virtual/?bounty=Vega%20Protocol)**. This website is where teams must register and then submit final challenge code etc. 

Note: Anyone can enter the Virtual Hackathon, we'd love to have you join in!

# On using the Fairground Testnet 🎢

Most of the code you'll write will target the **[Vega Fairground testnet](https://fairground.wtf)**, this is an **experimental network** free from the risks of real trading, Fairground is a safe and fun place to try out Vega yourself. Note, however that Fairground is an experimental network and running a version of Vega which is to be treated as alpha software. Crashes, unexpected quirks or issues can occur! We hope you'll participate in helping to find bugs and battle harden Vega. If you do spot something, please help reporting it either directly to us or via the [Nolt issue tracker](https://vega-testnet.nolt.io). Thank you!

# General Support & Resources

We're an exciting DEFI / blockchain project with an experimental testnet on which the team are adding new features all the time. Therefore, we'd love anyone interested in completing our ETHDenver bounties to get to know the testnet first. We feel it is very important for you test out the software, check out our documentation and understand the way the protocol works to complete the bounties to a high standard. We aim to be friendly and helpful, so don't be afraid to ask questions on Discord or in person - during the hackathon drop **Chris | Vega** or any of the community team a message if you want to meet up.

* **Please visit us on the [Official Vega Discord](https://vega.xyz/discordo) server channel:** `Developers > #eth-denver-hackathon`
* **[Vega Wallet](https://github.com/vegaprotocol/vegawallet/)** - CLI/Command line wallet needed to interact with Vega networks
* **[Fairground Testnet documentation](https://docs.fairground.vega.xyz)** - Guides, documentation, code snippets on integrating with Vega using the Fairground network.
* **[Vega Sample API Scripts](https://github.com/vegaprotocol/sample-api-scripts/)** - How to example API scripts for many of the features on Vega, in Python and more.
* **[Vega Protocol Specs](https://github.com/vegaprotocol/specs/tree/main/protocol#fundamental-concepts)** - Specifications, fundamentals and detailed documentation on the Vega protocol itself (deeper than the whitepaper)
* **[Vega Console on Fairground](https://console.fairground.wtf)** - UI/dAPP to interact with trading markets on Vega
* **[Fairground Testnet microsite](https://fairground.wtf)** - The official Vega testnet called Fairground, go here to start hacking with Ropsten ERC-20 test assets
* **[SporkDAO Discord](https://discord.gg/sporkdao)** - Official ETHDenver SporkDAO discord, please join and contribute or ask questions from the team in the #vega channel
* **[Vega Whitepaper](https://vega.xyz/papers/vega-protocol-whitepaper.pdf])** - The official Vega Protocol whitepaper

<img src="https://github.com/vegaprotocol/brand/raw/main/1-Vega-Brand-Basics/1G-Hixel/Vega_Hixel_Black.png" width="30%" alt="Hixel says Hi!" title="Hixel says Hi!" />
