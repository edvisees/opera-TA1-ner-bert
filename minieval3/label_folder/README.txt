       AIDA Phase 1 Evaluation Topic Annotations - UNSEQUESTERED - V2.0
                               LDC2019E77

                       Linguistic Data Consortium
                            October 21, 2019

0.1 Changes in V2.0

Annotations and documentation for topic E101 - Suspicious Deaths and
Murders in Ukraine (January-April 2015) have been added.

1. Introduction

This package contains annotations for the unsequestered documents for
the SM-KBP/AIDA 2019 eval. These annotations represent "stage 1",
"stage 2", and "stage 3" of the annotation process.

- stage 1 consists of annotation of salient mentions of events and
  relations with local mentions of their arguments).

- stage 2 consists of quality control on existing annotations, plus
  new annotations of informative mentions of arguments and annotation
  of any additional, salient event or relation mentions identified
  during quality control.

- stage 3 consists of linking entity mentions to a KB, and performing
  cross-doc, cross-lingual clustering of NIL entity, event, and
  relation mentions. Although there are three linking tab files (one
  for each topic), KB linking and NIL clustering are cross-topic.

Topics covered in this annotation:
E101 - Suspicious Deaths and Murders in Ukraine (January-April 2015)
E102 - Odessa Tragedy (May 2, 2014)
E103 - Siege of Sloviansk and Battle of Kramatorsk (April-July 2014)

2. Directory Structure and Content Summary

The directory structure and contents of the package are summarized
below -- paths shown are relative to the base (root) directory of the
package:

  data/                   -- contains subdirectories of annotation by topic
        E101/		  -- subdirectories containing annotation files
                             (see content description below)
        E102/             -- subdirectories containing annotation files
                             (see content description below)
        E103/             -- subdirectories containing annotation files
                             (see content description below)
  docs/                   -- contains documentation about the annotation
                             (see content description below)

2.1 Content Summary

This release contains annotation for a total of 224 unique documents,
with the following distribution across the three eval topics and
languages:

Topic ID    Language   Documents
E101        ENG        17
E102        ENG        24
E103        ENG        29
E101        RUS        36
E102        RUS        35
E103        RUS        41
E101        UKR        16
E102        UKR        16
E103        UKR        33
E103        UND         1

NOTE: Some documents are multilingual, so they are represented in the
docs/doc_lang_topic.tab file multiple times. See section 2.2 for a
listing of these multilingual documents and their associated
languages.

2.2 Documents with multiple languages

The following documents are multi-lingual, and thus appear more than
once in the docs/doc_lang_topic.tab file:

- Multilingual documents with 3 different languages:
IC0015YD1 (E103 - ENG, UKR, UND)
IC0015YD8 (E103 - ENG, RUS, UKR)
IC0015YG7 (E103 - ENG, RUS, UKR)
IC00162L9 (E103 - ENG, RUS, UKR)
IC001659G (E102 - ENG, RUS, UKR)

- Multilingual documents with 2 different languages:
IC0015LQN (E102 - ENG, RUS)
IC0015MVH (E101 - ENG, RUS)
IC0015NGX (E102 - ENG, RUS)
IC0015NIQ (E102 - ENG, UKR)
IC0015PG0 (E102 - RUS, UKR)
IC0015Y36 (E103 - ENG, UKR)
IC00162GK (E103 - ENG, UKR)
IC00163VF (E101 - ENG, RUS)
IC00164QG (E101 - ENG, RUS)
IC00169X6 (E103 - RUS, UKR)
IC0016ACK (E103 - RUS, UKR)
IC0016AE1 (E103 - RUS, UKR)
IC0016AIM (E103 - RUS, UKR)
IC0016ASA (E103 - RUS, UKR)

3. Annotations

The formats of annotations are described in the
AIDA_phase_1_table_field_descriptions_v4.tab file in the docs/
directory; the sections below provide descriptions of the content of
each type of annotation file, with some notes about differences from
the seedling annotation.

3.1 Mentions

There are three mentions tables for each topic: one for entities and
fillers, one for relations, and one for events. These tables contain
information about each annotated mention. Note that a KB-id is no
longer included in the mentions.tab files, as the KB linking
information is now contained in a separate linking tab file (see
below).

Differences between the mentions.tab files in the new Phase 1 format
and the seedling format include:

- Entity and filler mentions are now in a file called
  TOPICID_arg_mentions.tab (rather than the ent_mentions.tab files found
  in the seedling).

- All mentions.tab files now include subtype and subsubtype fields.

- All mentions.tab files now include the root uid instead of the tree
  id (no need to map to root uid through the tree id in order to match
  annotations to root documents).

- Video mentions now specify the signal type (picture or sound), and
  video and audio mentions include start and end time stamps for the
  mentions.

- Video "picture" mentions now include keyframe id; images and video
  "picture" mentions now include bounding box coordinates.

- Arg mentions include a mention status of "base" or "informative"
  indicating whether the entity/filler mention is the local mention
  that occupies an arg slot in a relation or event mention ("base") or
  whether it is an additional mention of an entity that is not local
  to the event/relation mention ("informative").

- Relation and event mentions can have the attributes "hedged" and/or
  "not". Other attribute types have been eliminated as they are now
  covered by relation types.

3.2 Slots

There are two slots tables per topic, one for relations and one for
events. Relation and event mentions in the mentions tables must be
looked up in the slots tables to find the arguments and fillers
involved in the relation/event.

Differences between the slots.tab files in the new Phase 1 format and
the seedling format include:

- Root uid replaces tree id as described in the mentions section
  above.

- Slot type labels use the new role labels from the AIDA annotation
  ontology, prefaced by indicators of the relation/event type and arg
  number. For example the slot type "rel022arg02sponsor" refers to the
  arg 2 sponsor role in the relation that has index number ldc_rel_022
  in the annotation ontology). To strip the slot_type to the bare role
  label, the first 11 characters can be removed, as this is a
  fixed-width preface.

- Argument mention ids have replaced the entity-level argument ids
  from the seedling annotation. The argmention_ids in the slots table
  correspond to "base" mentions in the arg_mentions table. Note that
  events which serve as arguments of sponsorship relations appear in
  the event mentions table, not the arg mentions table.

3.3 KB Linking

The KB linking tables provide a KB ID or NIL ID for each entity,
relation, and event mention. The KB IDs refer to AIDA Phase 1
Evaluation Reference Knowledge Base (LDC2019E43).

Note that this separate linking table means that KB IDs are not
present in the mentions.tab files.

Also note that in the case where annotators cannot disambiguate
between two or more possible KB links, multiple IDs are presented,
separated by a pipe ("|") symbol.


4. Documentation

The following documents are present in the ./docs directory of this package:

AIDA_Annotation_Guidelines_Quality_Control_and_Informative_Mentions_V1.0.pdf
- current annotation guidelines for "stage 2" of the annotation
process.

AIDA_Annotation_Guidelines_Salient_Mentions_V1.0.pdf - current
annotation guidelines for "stage 1" of the annotation process.

AIDA_phase_1_table_field_descriptions_v4.tab - description of the
structure of each type of annotation table. This table includes
information about column headers, content of each field, and format of
the contents.

doc_lang_topic.tab - provides the root uid, language, and topic for
each document with annotations present in this release.

LDC_AIDAAnnotationOntologyWithMapping_V8.xlsx - a copy of the
annotation ontology.

media_list.tab - provides the child uid and media type for all
non-text assets cited as provenance in the annotations present in this
release.

E101_E102_E103_topic_description.pdf - descriptions of E101, E102,
and E103 topics with queries and query IDs. Note that the queries are
meant to draw annotators attention to expected points of informational
conflict within the topic, but salience to the topic is defined more
broadly than simply providing the answer to one of the queries. See
the annotation guidelines for instructions provided to annotators on
determining salience.

{E101,E102,E103}_prevailing_theories_final.xlsx - these three files
contain prevailing theories for topics E101, E102, and E103
respectively.

eval_tracer_docs.tab - list of documents in the release with
exhaustive annotation of salient entities

5. Prevailing Theories

In the prevailing theories files, we provide a handful of natural
language prevailing theories about "what happened" for each topic, and
indicate which KEs are required for each theory. Note that prevailing
theories are *NOT* intended to exhaustively cover the possible
topic-level hypotheses that might emerge from the data.

Prevailing theories are in excel files, one file per topic, with one
prevailing theory per tab. Each KE within a prevailing theory has 
either a KB ID or a PT clustering ID.

Each tab contains information at the top with the topic and natural
language version of the theory. Below the natural language version is
a matrix of KEs that are required to fully support the theory, where a
KE is an event or relation with all its arguments. The first column
assigns an ID number to each of the KEs, the purpose of which is to
make it easy to sort and tell which arguments go together under a
particular relation or event. For each of the KEs, one line represents
the event or relation itself, and each argument is listed on a
separate line under the event/relation.

There are two columns containing KB IDs:

- Column C (Event/Relation KB ID) contains the KB ID or clustering ID
  for the event or relation

- Column I (Item KE) contains the KB ID or clustering ID for the 
  argument populating the given event or relation slot.

Entity and relation KEs that do not appear in the AIDA eval topic 
KB (LDC2019E43) have PT clustering IDs formatted like PTE_E10#_### 
(for prevailing theory entities) or PTR_E10#_### (for prevailing theory 
relations). These IDs provide clustering information for the prevailing
theories of the given topic. These are not NIL IDs, in that they do
not correspond to any annotations in ./data, and only indicate which
KEs within a topic's prevailing theories are coreferent.

Event KEs within the prevailing theories all have NIL IDs. These IDs
may also be present in the kb_linking.tab files in ./data, meaning
they may have corresponding mention-level annotations.

In addition to the KB IDs, each line has information about the type,
subtype, and sub-subtype of each event/relation/argument as well as
expected date, start date range, end date range, and attribute
information where known.


6. Known Issues

Duplicate arg mentions -- Some arg mentions may be annotated more than
once when they appear as arguments of more than one relation/event;
that is, the same type, subtype, and sub-subtype may be applied to the
same text extent (or video/image provenance) more than once. Note that
duplicate arg mentions each have a unique argmention_id.

Mentions missing text info -- There are 6 relation mentions and 13
entity mentions missing textoffset_startchar, textoffset_endchar, and
text_string information:

Entity mentions missing mention level -- There are 13 entity mentions
missing mention_level information.

Orphaned base arg mentions -- There are 181 base arg mentions
that are not annotated as a slot in an event or relation.


7. Copyright Information

   (c) 2019 Trustees of the University of Pennsylvania


8. Contact Information

Stephanie Strassel <strassel@ldc.upenn.edu> AIDA PI
Jennifer Tracey <garjen@ldc.upenn.edu> AIDA Project Manager

----
README created by Kira Griffitt on September 19, 2019
README updated by Kira Griffitt on September 23, 2019
README updated by Kira Griffitt on September 25, 2019
README updated by Kira Griffitt on October 17, 2019
README updated by Kira Griffitt on October 21, 2019
